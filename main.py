from views.login_view import LoginView
import customtkinter as ctk

if __name__ == "__main__":
    ctk.set_appearance_mode("blue")
    ctk.set_default_color_theme("green")

    app = LoginView()
    app.mainloop()
