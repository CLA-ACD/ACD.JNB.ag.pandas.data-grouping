import pandas as pd

from learntools.core import *

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv", index_col=0)

class Ejercicio1(EqualityCheckProblem):
    _var = 'p1'
    _expected = (
            df.groupby('Age').Age.count(),
    )

class Ejercicio2(EqualityCheckProblem):
    _var = 'p2'
    _expected = (
            df.groupby('Pclass').Age.min(),
    )

class Ejercicio3(EqualityCheckProblem):
    _var = 'p3'
    _expected = (
            df.groupby('Embarked').Age.agg(["min", "max"]),
    )

class Ejercicio4(EqualityCheckProblem):
    _var = 'p4'
    _expected = (
            df.groupby(['Pclass', 'Sex']).Age.agg(["min", "max"]),
    )

class Ejercicio5(EqualityCheckProblem):
    _var = 'p5'
    _expected = (
            df.sort_values(by=['Age']),
    )

class Ejercicio6(EqualityCheckProblem):
    _var = 'p6'
    _expected = (
            df.sort_values(by=['Survived', 'Pclass']),
    )

class Ejercicio7(EqualityCheckProblem):
    _var = 'p7'
    _expected = (
            df.Name.dtype,
    )

class Ejercicio8(EqualityCheckProblem):
    _var = 'p8'
    _expected = (
            df.dtypes,
    )

class Ejercicio9(EqualityCheckProblem):
    _var = 'p9'
    _expected = (
            df[pd.isnull(df.Cabin)],
    )

class Ejercicio10(EqualityCheckProblem):
    _var = 'p10'
    _expected = (
            df.rename(columns={'Pclass' : 'PassengerClass'}),
    )


qvars = bind_exercises(globals(), [
    Ejercicio1,
    Ejercicio2,
    Ejercicio3,
    Ejercicio4,
    Ejercicio5,
    Ejercicio6,
    Ejercicio7,
    Ejercicio8,
    Ejercicio9,
    Ejercicio10,
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)