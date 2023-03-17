import 'package:app_getx_tutorial/controllers/DetailsController.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class DetailsPage extends StatelessWidget {
  const DetailsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Details Page'),
          centerTitle: true,
          automaticallyImplyLeading: true,
          backgroundColor: Colors.black,
        ),
        body: GetBuilder<DetailsController>(
            init: DetailsController(),
            builder: (_) {
              return Center(child: GetX<DetailsController>(builder: (_) {
                return Text(
                  "Details Page {controller.number}",
                  style: TextStyle(fontSize: 30),
                );
              }));
            }));
  }
}
