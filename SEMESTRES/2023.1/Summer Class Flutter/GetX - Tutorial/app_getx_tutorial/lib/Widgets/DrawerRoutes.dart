import 'package:flutter/material.dart';
import 'package:get/get.dart';

class DrawerNavegacaoRotas extends StatelessWidget {
  final List<Map<String, dynamic>> menuItems = [
    {'title': 'Como fazer Rotas com o Getx', 'route': '/Page1'},
    {'title': 'Gerenciamento de Estado com o Getx', 'route': '/Page2'},
  ];

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: [
          DrawerHeader(
            decoration: BoxDecoration(
              color: Colors.blue,
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Como funciona o Getx',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 18,
                  ),
                ),
                SizedBox(height: 15),
                Expanded(
                  child: ListView(
                    shrinkWrap: true,
                    children: [
                      ListTile(
                        title: Text('Informação 1'),
                      ),
                      ListTile(
                        title: Text('Informação 2'),
                      ),
                      ListTile(
                        title: Text('Informação 3'),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          ...menuItems.map((item) {
            return ListTile(
              title: Text(item['title']),
              onTap: () {
                Get.toNamed(item['route']);
              },
            );
          }).toList(),
        ],
      ),
    );
  }
}
