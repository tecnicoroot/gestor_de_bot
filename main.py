from views.login_view import LoginView
import customtkinter as ctk

if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    app = LoginView()
    app.mainloop()
