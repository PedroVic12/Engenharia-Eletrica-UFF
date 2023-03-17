import 'package:app_getx_tutorial/Widgets/DrawerRoutes.dart';
import 'package:app_getx_tutorial/pages/sc_HomePage.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

//!Frontend

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final ControllerGetX controller =
        Get.find(tag: 'controller'); // obtendo o controller usando a tag

    return Scaffold(
      appBar: AppBar(
        title: Text(controller.titulo),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.add),
            onPressed: () => controller.incrementarValor(),
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Contador com o GetX:',
              style: TextStyle(fontSize: 30),
            ),

            // usando o Obx para observar o valor do observável definido anteriormente
            Obx(() => Text(
                  '${controller.count.value}', // usando o valor do observável
                  style: const TextStyle(fontSize: 30),
                )),

            Card(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    'HomePage SummerClass',
                    style: TextStyle(fontSize: 30),
                  ),
                  ElevatedButton(
                    onPressed: () {
                      Get.to(HomePageSummerClass());
                      // arguments: 'Argumento passado para a pagina Details');
                    },
                    child: const Text(
                        'Ir para a Pagina Details Summer Class| Não funfa :('),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => controller.incrementarValor(),
        child: const Icon(Icons.add),
      ),
      drawer: DrawerNavegacaoRotas(),
    );
  }
}

//!Backend

//? Definimos o nosso controller
class ControllerGetX extends GetxController {
  // obs é uma extensão Getx para transformar em um observável
  var count = 0.obs;

  String titulo = 'Meu aplicativo com o Getx';

  void incrementarValor() {
    // value é uma propriedade do observável para acessar o valor
    count.value++;
    print('Contador: ${count.value}');
    update();
  }
}
