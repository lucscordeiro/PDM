import flet as ft
from CustomButton import CustomButton

def main(page: ft.Page):
    
    task = ft.TextField(label="Task")
    listTask = []
    
    # listTask = ft.List(items=task.value)

    def clickBtnAddTask(e):
        btnAddTask.addTask()
        listTask.append(task.value)
        print(listTask) 
        page.update()
    
    def clickBtnToogleVisibility(e):
        btnAddTask.toogleVisibility()
        page.update()
    
    def clickBtnClearList(e):
        btnAddTask.clearList()
        page.update()

    btnAddTask = CustomButton(
        text = "Add",
        bgcolor = ft.colors.BLUE,
        color = ft.colors.WHITE,
        on_click=clickBtnAddTask,
        icon=None
    )
    
    btnToogleVisibility = CustomButton(
        text = "Visibility",
        bgcolor = ft.colors.GREEN,
        color = ft.colors.WHITE,
        on_click=clickBtnToogleVisibility,
        icon=None
    )

    btnClearList = CustomButton(
        text = "Clear",
        bgcolor = ft.colors.RED,
        color = ft.colors.WHITE,
        on_click=clickBtnClearList,
        icon=None
    )

    page.add(task, btnAddTask, btnClearList, btnToogleVisibility)

ft.app(target=main)