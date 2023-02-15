import mechanize
from io import StringIO
import pandas as pd

def queryMillennium(base='Guo2010a',xlim=[0,63],ylim=[0,63],zlim=[0,63],snapnum=63):
  '''
  Retrieves the simulation from garching public repository 
  ---------------------------------------------------
  base -  base study: 'DeLucia2006a' or 'Guo2010a'
            'DeLucia2006a' - https://ui.adsabs.harvard.edu/abs/2007MNRAS.375....2D/abstract
            'Guo2010a' - https://ui.adsabs.harvard.edu/abs/2011MNRAS.413..101G/abstract 
  xlim - spatial limits [10,20]
  ylim - spatial limits [10,20]
  zlim - spatial limits [10,20]
  snapnum - snasphot number (between 0 and 63)
  ---------------------------------------------------
  returns pandas dataframe 
  '''

  br = mechanize.Browser()
  br.open("http://gavo.mpa-garching.mpg.de/Millennium/MyDB")
  br.select_form(nr=0)
  br.form["SQL"] = f"select x,y,z,redshift from millimil..{base} where snapnum={snapnum} and x between {xlim[0]} and {xlim[1]} and y between {ylim[0]} and {ylim[1]} and z between {zlim[0]} and {zlim[1]}"
  response = br.submit()
  #str(response.read())
  response = str(response.read().decode('utf-8'))
  response = response.replace('\\n', '\n')
  #reponse = response.replace('')
  df = pd.read_csv(StringIO(response),comment='#')
  return df.dropna()
