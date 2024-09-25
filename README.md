# Langton's Ant

Implementation of Langton's Ant cellular automata in Python.

## Configuration
The software is based on some configuration parameters to be set as environmental variables (or directly in the code):

* `WIDTH`: the width of the grid - default is 1280
* `HEIGHT`: the height of the grid - default is 720
* `RESOLUTION`: the resolution of the grid cells - default is 5
* `RULE`: the rule to be applied to the ant - default is RL

The RULE parameter is a string of N parameters describing the behaviour of the ant. The first two colors are black and white respectively, and the following N-2 colors are randomly generated.

## How to run

Install the dependencies:

```python
pip install -r requirements.txt
```

run the script:

```python
python ant.py
```

## Examples

### Rule: RL
![Example of Langton's Ant with Rule RL](images/RL_example.png)

### Rule: LLRR
![Example of Langton's Ant with Rule RL](images/LLRR_example.png)

### Rule: LRRRRRLLR
![Example of Langton's Ant with Rule RL](images/LRRRRRLLR_example.png)
