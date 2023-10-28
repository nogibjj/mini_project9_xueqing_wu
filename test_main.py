from main import read_file, summary, summary_plot
import matplotlib.pyplot as plt

"Test the dataset summary"


def test_read_file():
    df=read_file('imdb_top_1000.csv')
    # assert not df.empty()
    assert len(read_file('imdb_top_1000.csv'))==1000

def test_describe():
    describe=read_file('imdb_top_1000.csv')
    assert describe['IMDB_Rating'].mean()==7.949299999999999
    # assert describe['IMDB_Rating']['max']==9.3

def test_graph():
    df=read_file('imdb_top_1000.csv')
    plt.hist(df['IMDB_Rating'])
    plt.show()



if __name__ == "__main__":
    test_read_file()
    test_describe()
    test_graph()


