import 'package:app_getx_tutorial/controllers/HomeController.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class HomePageSummerClass extends GetView<HomeController> {
  const HomePageSummerClass({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Home Page App Bar'),
          centerTitle: true,
          actions: [
            IconButton(
              icon: const Icon(Icons.refresh_sharp),
              onPressed: () => controller.reloadData(),
            ),
          ],
          backgroundColor: Colors.black,
        ),
        body: GetBuilder<HomeController>(builder: (_) {
          return Center(
            child: controller.isLoading
                ? const CircularProgressIndicator()
                : ElevatedButton(
                    onPressed: () => {},
                    child: null,
                  ),
          );
        }));
  }
}
