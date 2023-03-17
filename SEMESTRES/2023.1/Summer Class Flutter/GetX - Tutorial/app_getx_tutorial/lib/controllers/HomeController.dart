//Summer Class

import 'package:app_getx_tutorial/routes/AppRoutes.dart';
import 'package:get/get.dart';

class HomeController extends GetxController {
  bool isLoading = true;

  var obj = ''.obs;

  void onPressedButton() {
    Get.toNamed(Routes.DETAILS);
  }

  @override
  void onInitMyApp() {
    fetchData();
    //super.onInitMyApp();
  }

  //! Aqui fazemos a chamada para o repositorio usando Boas praticas com Encapulamento
  void fetchData() {
    isLoading = true;
    update();

    //Call Repor to Fetch data
    Future.delayed(const Duration(seconds: 3)).then((value) {
      isLoading = false;
      update();
    });
  }

  void reloadData() {
    fetchData();
  }
}
