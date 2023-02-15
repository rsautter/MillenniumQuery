# Millennium Query
This package downloads the public [Millennium](https://wwwmpa.mpa-garching.mpg.de/millennium/) simulation data using [mechanize](https://github.com/sparklemotion/mechanize).

To install (colab):

    !pip install mechanize
    !pip install git+https://github.com/rsautter/MillenniumQuery

Example of plot:

    import matplotlib.pyplot as plt
    data = queryMillennium(snapnum=57)
    fig=plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(data['x'],data['y'],data['z'],alpha=0.05,s=10)
    ax.view_init(elev=45., azim=45)
    plt.title("Z = "+str(data['redshift'][0]),fontsize=15,weight='bold',loc='right')
    plt.tight_layout()
    plt.show()
    
<img src="https://raw.githubusercontent.com/rsautter/MillenniumQuery/main/imgs/example.png" width=60% height=60%>
