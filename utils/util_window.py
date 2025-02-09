def center_window(window,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = window.winfo_screenwidth()
    pantall_largo = window.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return window.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")