def get_project_data_dir():
    return '/Users/pedro/scale_interaction_in_gsam/data/'

def get_project_fig_dir():
    return '/Users/pedro/scale_interaction_in_gsam/figures/'
def save_figure(fig, name):
    path = get_project_fig_dir() + name
    fig.savefig(path, format='pdf', bbox_inches="tight")