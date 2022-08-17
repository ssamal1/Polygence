import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(
    external_stylesheets=[dbc.themes.JOURNAL]
)

body = dbc.Container([ 
dbc.Row(
            [
            html.H1(children='COVID Hotspot and Funding Analysis in California', style = {'marginTop':100, "width": "70%", 'textAlign': 'center'}),
            html.H4(children='In which counies around California are the COVID hotspots, coldpspots, and how havs the counties in those areas spent their money.', style = {'marginTop':5, 'textAlign': 'left', "width": "60%"}),
            html.H6(children='By Sanat Samal', style = {'marginTop':5, "width": "60%", 'textAlign': 'left', 'color':'blue'}),
            html.Img(src='https://www.evergreenhealth.com/app/files/public/3768/covid-19-testing-banner.jpg', style={'marginTop':5, "width":"60%"}),
            html.H3(children='Modeling COVID Hotspots', style = {'width':'60%', 'marginTop':40}),
            html.P(children='I have modeled COVID hotspots in California to show which counties have had larger issues with COVID. I have used Morans Statistic to model these hotspots. This means that the hotspots are decided relative to the neighboring counties. Hence the hotspots do not represent where the most COVID is, but rather where COVID has clustered relative to surrounding areas in simple terms. It also says where COVID has not clustered. The hotspots are decided based on z-score and p-value. These statistical figures tell us a values relationship to the other values, and the chance that the numbers are following a trend, and are not simply random. This way the hotspots and coldspots are only made from data that is statistically significant.', style = {'width':'60%', 'marghinTop':5}),
            html.P(children='In the Morans Statistic algorithm the inputed weights for each county was decided by the K Nearest Neighbor Weighted machine learning algorithm. This model weights the surrounding datapoints by the distance from the instance datapoint (the county being measured). In this manner we cna judge COVID rates based on the surrounding counties.', style = {'width':'60%', 'marghinTop':5}),
            html.P(children='To see the change in hotspots, we found the hotspots on a dual monthly basis from March 2020 to December 2021:', style = {'width':'60%', 'marghinTop':5}),
            




            html.P(children='As we can see above, the northern counties of Lassen, Shasta, Sierra, Yube, Placer, Tehama and Del Norte are commonly hotspots. On the other hand the coldspots are often Mariposa, Alpine, and San Mateo from March 1st 2020 to February 28 2021. From March to October of 2021 we can see that the previously hot counties of Lassen, Shasta, Sierra, Yube, Placer, Tehama and Del Norte have become colder. On the other hand Los Angeles county has become a hotspot.', style = {'width':'60%', 'marghinTop':5}),

            html.H3(children='COVID Funding', style = {'width':'60%', 'marginTop':40}),
            html.P(children='Among the counties that went to COVID hotspots, their funding patterns are charted below:', style = {'width':'60%', 'marghinTop':5}),
            html.P(children='The Los Angeles County funding graph is below:', style = {'width':'60%', 'marghinTop':5}),
            
            html.P(children='As we can see the counties that use more preventative measures, such as funding COVID workers have fared better than those focusing on reactive measures such as contact tracing and covid testing', style = {'width':'60%', 'marghinTop':5})
            ], justify="center", 
            )],style={"height": "100vh"}

)


   
    
app.layout = html.Div([body])   
    


if __name__ == "__main__":
    app.run_server()