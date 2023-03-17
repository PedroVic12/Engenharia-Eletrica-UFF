//SummerClass

import 'package:app_getx_tutorial/controllers/DetailsController.dart';
import 'package:get/get.dart';

class DetailsBinding implements Bindings {
  @override
  void dependencies() {
    Get.put(() => DetailsController());
  }
}
