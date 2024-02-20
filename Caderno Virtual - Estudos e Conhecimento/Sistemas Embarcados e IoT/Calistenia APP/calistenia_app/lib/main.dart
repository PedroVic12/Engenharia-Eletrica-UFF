import 'package:flutter/material.dart';
import 'package:web_socket_channel/io.dart';
import 'package:camera/camera.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;
  final _channel = IOWebSocketChannel.connect('ws://localhost:8765');

  @override
  void initState() {
    super.initState();
    _initCamera();
  }

  void _initCamera() async {
    final cameras = await availableCameras();
    final firstCamera = cameras.first;

    _controller = CameraController(
      firstCamera,
      ResolutionPreset.medium,
    );

    _initializeControllerFuture = _controller.initialize();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: FutureBuilder<void>(
          future: _initializeControllerFuture,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              // Se a câmera estiver inicializada, exibe a visualização da câmera.
              return CameraPreview(_controller);
            } else {
              // Caso contrário, exibe um indicador de carregamento.
              return Center(child: CircularProgressIndicator());
            }
          },
        ),
        floatingActionButton: FloatingActionButton(
          child: Icon(Icons.camera_alt),
          onPressed: () async {
            try {
              // Aguarda a inicialização da câmera
              await _initializeControllerFuture;

              // Captura a imagem
              final image = await _controller.takePicture();

              // Envie a imagem para o servidor WebSocket aqui
              // Você precisará converter a imagem em um formato que possa ser enviado (por exemplo, base64)
              _channel.sink.add(image.path); // Exemplo simplificado
            } catch (e) {
              print(e); // Trata erro de captura de imagem
            }
          },
        ),
      ),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    _channel.sink.close();
    super.dispose();
  }
}
