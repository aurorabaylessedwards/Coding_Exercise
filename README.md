# CSI Coding Exercise -- Aurora

Finds the nearest tall building to each random point around Portland, OR (see [G. Berardinelli's instructions](https://gist.github.com/gberardinelli/8567cdbcad220e46b2f8fc4e33a203a0)). 

This project is written in Python 3. If you do not have Python 3, I suggest downloading 64-Bit Python 3.7 [Anaconda](https://www.anaconda.com/products/individual) with [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows). 

Additionally, you will need git/github set up in PyCharm. This [video](https://www.youtube.com/watch?v=NhFRpFtiHec) is a great resource to walk you through the process of setting up git/github, additionally [PyCharm has some doccumentation on the process](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html).

To set up the project open PyCharm using the Anaconda Navigator. 

![open_pycharm](/images/open_pycharm.png?raw=true "open PyCharm")

Select 'Get from Version Control' and paste the URL of this project. **https://github.com/aurorabaylessedwards/CSI_Coding_Exercise.git**

## You will see an error in the top right hand corner of the screen prompting you to set up your python interpreter for the project. 
![err](/images/error.png?raw=true "error_pic")

Set up an interpreter in python 3.x (7 or 8). 

![configure_interpreter](/images/configure_interpreter.png?raw=true "configure interpreter")

## Download the packages you need [geopandas](https://geopandas.org/install.html), [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html), and [shapely](https://pypi.org/project/Shapely/).

![install_packages](/images/install_packages.png?raw=true "install packages")

Now, you should be able to run `coding_exercise.py` and `neighbors_in_specified_distance.py` without errors. The output of this script will print some information to the python console including the location of output shapefiles. By default these are written to the `CSI_Coding_Exercise` folder created as part of the cloning process. However, you can change the output directory by changing the path at the beginning of the script. 


Please, reach out if you have any questions to abayless-edwards at QSI. 

Thanks!
