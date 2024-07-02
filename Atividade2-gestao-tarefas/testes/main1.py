import flet as ft
from CustomButton import CustomButton  # Assuming CustomButton is correctly implemented

def main(page: ft.Page):
    listTask = []

    task = ft.TextField(label="Task", width=300)
    listDisplay = ft.Text(value="", visible=True)
    
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("TASK")),

        ],
        # rows=[
        #         ft.DataRow(

        #         )
        # ]
    )

    def updateListDisplay():
        # Update the displayed text with items from the list
        listDisplay.value = "\n".join(listTask)

    def clickBtnAddTask(e):
        taskText = task.value.strip()
        if taskText:
            listTask.append(taskText)
            task.value = ""  # Clear the text field
            updateListDisplay()
            page.update()

    def clickBtnToogleVisibility(e):
        listDisplay.visible = not listDisplay.visible
        page.update()

    def clickBtnClearList(e):
        listTask.clear()
        updateListDisplay()
        page.update()

    btnAddTask = CustomButton(
        text="Add",
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE,
        on_click=clickBtnAddTask,
        icon=None
    )

    btnToogleVisibility = CustomButton(
        text="Toggle Visibility",
        bgcolor=ft.colors.GREEN,
        color=ft.colors.WHITE,
        on_click=clickBtnToogleVisibility,
        icon=None
    )

    btnClearList = CustomButton(
        text="Clear List",
        bgcolor=ft.colors.RED,
        color=ft.colors.WHITE,
        on_click=clickBtnClearList,
        icon=None
    )

    # Add components to the page
    page.add(task, listDisplay, table, btnAddTask, btnToogleVisibility, btnClearList)

# Launch the app with the main function as the target
ft.app(target=main)
