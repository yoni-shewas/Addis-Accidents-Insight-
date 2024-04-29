import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def vehicle_distribution(df):

    # Create histogram using Plotly
    histogram = go.Histogram(x=df['Type_of_vehicle'], nbinsx=20)

    fig = make_subplots(rows=1, cols=1)

    # Add histogram trace to subplot
    fig.add_trace(histogram, row=1, col=1)

    # Update layout
    fig.update_layout(title='vehicle type Distribution',
                      xaxis_title='Vehicle type', yaxis_title='Frequency')

    # Save plot to HTML file
    plotly_html = fig.to_html(full_html=False)

    # Write HTML file
    with open('./analysis_visualization_outputs/vehicle_type_distribution_graphs.html', 'w') as f:
        f.write(plotly_html)


if __name__ == '__main__':
    # load cleanded data
    RTAcleaned = "../cleaned_data/RTA-Dataset-cleaned.csv"

    df = pd.read_csv(RTAcleaned)

    # perform analysis
    vehicle_distribution(df)
