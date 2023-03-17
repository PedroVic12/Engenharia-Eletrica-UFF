//Summer Class CONTROLES TOTAL DE ROTAS!!! 

//Esse arquivo deve estar dentro de controllers

import 'package:app_getx_tutorial/bindings/details_binding.dart';
import 'package:app_getx_tutorial/bindings/home_binding.dart';
import 'package:app_getx_tutorial/pages/DetailsPage.dart';
import 'package:app_getx_tutorial/pages/Page1.dart';
import 'package:app_getx_tutorial/pages/sc_HomePage.dart';
import 'package:app_getx_tutorial/routes/AppRoutes.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../pages/HomePage.dart';

abstract class AppPages {
  static get pages => [
        GetPage(
            name: Routes.HOME, page: () => HomePage(), binding: HomeBinding()),
        GetPage(name: Routes.SPLASH, page: () => Pagina1()),
        GetPage(
            name: Routes.DETAILS,
            page: () => DetailsPage(),
            binding: DetailsBinding())
        //GetPage(name: Routes.HOME, page: () => HomePageSummerClass()),
        //GetPage(name: Routes.Splash, page: () => SplashPage()),
        //GetPage(name: Routes.DETAILS, page: () => DetailsPage()),
      ];
}
