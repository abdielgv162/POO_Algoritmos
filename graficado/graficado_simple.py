from bokeh.plotting import figure, output_file, show 
#Importar de bokeh.plotting 3 funciones
#Figure: ventana donde vamos a graficar
#Output_file: nos permite determinar el nombre del archivo a generar como output
#Show: genera un servidor que se prende y muestra el html para el browser (mostrar)


if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    # type(figure)
    # help(figure)

    total_vals = int(input('Cuantos valores se van a graficar? '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input('Valor Y para {x}: '))
        y_vals.append(val)
    
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
