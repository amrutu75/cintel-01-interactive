import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

#Add Page title
ui.page_opts(title="PyShiny App with Plot",fillable=True)

#Add sidebar with a slieder input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 25)


@render.plot(alt="A histogram showing random data distribution")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    plt.hist(x, input.selected_number_of_bins(), density=True)
