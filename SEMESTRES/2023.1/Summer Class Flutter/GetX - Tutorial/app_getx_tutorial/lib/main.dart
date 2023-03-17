import 'package:app_getx_tutorial/bindings/initial_binding.dart';
import 'package:app_getx_tutorial/pages/HomePage.dart';
import 'package:app_getx_tutorial/pages/Page1.dart';
import 'package:app_getx_tutorial/pages/Page2.dart';
import 'package:app_getx_tutorial/routes/AppPages.dart';
import 'package:app_getx_tutorial/routes/AppRoutes.dart';

import 'package:flutter/material.dart';
import 'package:get/get.dart';

void main() {
// Aqui registramos o controller para que ele possa ser acessado pelo Get.find()
  Get.put(ControllerGetX());

// adicionando o argumento tag para que possamos ter mais de um controller
  Get.put(ControllerGetX(), tag: 'controller');

//! Foema de mapear as rotas de forma padrao
  // runApp(GetMaterialApp(
  //   title: 'Getx Tutorial',
  //   initialRoute: '/',
  //   defaultTransition: Transition.fade,
  //   getPages: [
  //     GetPage(name: '/', page: () => HomePage()),
  //     GetPage(name: '/Page1', page: () => Pagina1()),
  //     GetPage(name: '/Page2', page: () => Pagina2()),
  //   ],
  // ));

  //SummerClass
  runApp(GetMaterialApp(
    debugShowCheckedModeBanner: true,
    defaultTransition: Transition.fade,
    initialRoute: Routes.HOME,
    getPages: AppPages.pages,
  ));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
// Definindo a rota inicial como a HomePage

    return GetMaterialApp(
      title: "Model App",
      initialRoute: Routes.SPLASH,
      getPages: AppPages.pages,
      initialBinding: InitialBinding(),
    );

    //!Outra forma de fazer o mapeamento das rotas
    // return GetMaterialApp(
    //   initialRoute: '/',
    //   getPages: [
    //     GetPage(name: '/', page: () => HomePage()),
    //   ],
    // );
  }
}
