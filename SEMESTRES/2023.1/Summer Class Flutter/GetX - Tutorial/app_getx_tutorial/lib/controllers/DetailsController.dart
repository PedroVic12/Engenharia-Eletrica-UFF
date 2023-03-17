//Summer Class --> Aula2.5

import 'package:app_getx_tutorial/routes/AppRoutes.dart';
import 'package:get/get.dart';

class DetailsController extends GetxController {
  //Variaveis observaveis e olhando as modificações que podem ter
  final _obj = ''.obs;
  set obj(value) => _obj.value = value;
  get obj => _obj.value;

  //Boas praticas com sua Navegação Capitão!
  final _number = 0.obs;
  set number(value) => _number.value = value;
  get number => _number.value;

  void onPressedButton() {
    number++;
  }
}
