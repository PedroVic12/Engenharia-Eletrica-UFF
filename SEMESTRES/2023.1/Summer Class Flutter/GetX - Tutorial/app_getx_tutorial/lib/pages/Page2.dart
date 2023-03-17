import 'package:flutter/material.dart';
import 'package:get/get.dart';

class Pagina2 extends StatelessWidget {
  const Pagina2({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Pagina 2'),
        backgroundColor: Colors.red,
      ),
      body: Column(
        children: [
          ElevatedButton(
            onPressed: () {
              //! Navegando para a pagina 2 usando o Getx
              Get.toNamed('/Page2');
            },
            child: Text('Ir para a Pagina 2'),
          ),
          Container(
            child: Center(
              child: Text('Bem vindo a Pagina 1!'),
            ),
          ),
        ],
      ),
    );
  }
}
