import flet as ft

def main(page: ft.Page):
    page.title = "MY TODO LIST"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.bgcolor = "#0D0714"
    page.scroll = ft.ScrollMode.HIDDEN
    page.appbar = ft.AppBar(
        title=ft.Text("My to do list", weight=ft.FontWeight.BOLD, size=20),
        bgcolor="#0D0714",
        center_title=True,
        color=ft.colors.WHITE,
    )

    tasks = []
    completed_tasks = []

    def add_task(e):
        task = ft.Checkbox(label=new_task.value, on_change=toggle_task)
        delete_button = ft.IconButton(
            icon=ft.icons.DELETE_FOREVER_ROUNDED,
            icon_color="pink600",
            icon_size=40,
            tooltip="Delete record",
            on_click=lambda _: delete_task(task_container)
        )
        task_container = ft.Container(
            content=ft.Row(
                [task, delete_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            margin=ft.Margin(top=5, right=70, bottom=5, left=70),
            border=ft.border.all(1, "lightgray"),
            border_radius=10,
            height=50,
            bgcolor="#251D30",
        )
        tasks.append(task_container)
        task_list.controls.append(task_container)
        new_task.value = ""
        page.update()

    def delete_task(task_container):
        if task_container in tasks:
            tasks.remove(task_container)
            task_list.controls.remove(task_container)
        if task_container in completed_tasks:
            completed_tasks.remove(task_container)
            completed_task_list.controls.remove(task_container)
        page.update()

    def toggle_task(e):
        task_container = e.control.parent.parent
        if e.control.value:
            if task_container in tasks:
                tasks.remove(task_container)
                task_list.controls.remove(task_container)
            completed_tasks.append(task_container)
            completed_task_list.controls.append(task_container)
        else:
            if task_container in completed_tasks:
                completed_tasks.remove(task_container)
                completed_task_list.controls.remove(task_container)
            tasks.append(task_container)
            task_list.controls.append(task_container)
        page.update()

    new_task = ft.TextField(
        hint_text="Add a new task",
        width=1000,
        border_color="blue",
        bgcolor="lightgray",
    )
    add_button = ft.FloatingActionButton(
        icon="add",
        on_click=add_task,
        bgcolor="blue",
        width=70,
    )

    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[new_task, add_button],
        spacing=10,
    )

    task_list = ft.Column()
    completed_task_list = ft.Column()

    page.add(row)
    page.add(ft.Text("Tasks:", size=20, weight=ft.FontWeight.BOLD, color="white"))
    page.add(task_list)
    page.add(ft.Text("Completed Tasks:", size=20, weight=ft.FontWeight.BOLD, color="white"))
    page.add(completed_task_list)

ft.app(main)