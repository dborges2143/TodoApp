import 'package:flutter/material.dart';
import 'package:todoapp/models/classes/task.dart';
import 'package:todoapp/models/global.dart';
import 'package:todoapp/widgets/intray_todo_widget.dart';

class IntrayPage extends StatefulWidget {
  @override
  _IntrayPageState createState() => _IntrayPageState();
}

class _IntrayPageState extends State<IntrayPage> {
  List<Task> taskList = [];

  @override
  Widget build(BuildContext context) {
    taskList = getList();
    return Container(
      color: darkGreyColor,
      child: Theme(
        data: ThemeData(
          canvasColor: Colors.transparent
        ),
        child: ReorderableListView(
          padding: EdgeInsets.only(top: 300),
          children: _buildReorderableListChildren(),
          onReorder: _onReorder,
        ),
      ),
    );
  }

  List<Widget> _buildReorderableListChildren() {
    return getList().map((Task item) =>
        ListTile(
            key: Key(item.taskId),
            title: IntrayTodo(title: item.title)
        )).toList();
  }

  void _onReorder(oldIndex, newIndex) {
    setState(() {
      Task item = taskList[oldIndex];
      taskList.remove(item);
      taskList.insert(newIndex, item);
    });
  }

  List<Task> getList() {
    for (int i = 0; i < 10; i ++) {
      taskList.add(Task("My first todo " + i.toString(), false, i.toString()));
    }
    return taskList;
  }
}