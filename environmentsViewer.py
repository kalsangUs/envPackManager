import tkinter as tk
from environmentManager import EnvironmentManager
from environmentReader import EnvironmentReader


def load():
    manager = EnvironmentManager()
    reader = EnvironmentReader()
    manager.setEnviromentReader(reader)
    manager.loadCondaEnvironments()
    manager.loadVirtualEnvironments()
    return manager.getEnvironments()


class EnvironmentsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Environments")
        self.root.geometry("400x600")
        self.root.configure(bg='white')
        envs = load()

        # Main frame
        main_frame = tk.Frame(root, bg='white', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(
            main_frame,
            text="Environments",
            font=('Inter', 24, "bold"),
            bg='white',
            fg='black'
        )
        title_label.pack(pady=(0, 20))

        for env in envs:
            btn = tk.Label(
                main_frame,
                text=env.getName(),
                font=('Inter', 18, 'normal'),
                bg='#FF5B5B',  # Red color
                fg='white',
                height=2,
                cursor='arrow'
            )
            btn.pack(fill=tk.X, pady=(0, 10))

            # Click event
            btn.bind("<Button-1>", lambda e,
                     env=env: self.on_environment_click(env))

            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#FF3B3B'))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg='#FF5B5B'))

    def on_environment_click(self, environment):
        print(f"Selected environment: {environment}")


def main():
    root = tk.Tk()
    app = EnvironmentsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
