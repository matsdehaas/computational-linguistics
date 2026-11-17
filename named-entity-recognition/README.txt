The file build_models.py is called in a terminal by “python build_models.py”
To see the possible arguments you can use “python build_models.py”

The arguments are:
--pickle - the path to write the file to (e.g. best.pickle)			**this argument is requires
--dataset - the dataset used to train the model (e.g. ned.train)	**this argument defaults to ned.train if empty
--features - the feature extraction function used (e.g. test_features) **this argument defaults to test_features if empty

examples:

“python build_models.py --pickle best.pickle --dataset ned.train --features test_features1” 
or
“python build_models.py --pickle best.pickle --dataset ned.train” 
or
“python build_models.py --pickle best.pickle”
