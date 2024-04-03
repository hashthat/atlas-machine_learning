    Sigmoid: The sigmoid function squashes the input to a value between 0 and 1. It's expressed as:
    σ(x)=11+e−xσ(x)=1+e−x1​
    Sigmoid functions are useful in binary classification tasks where the output needs to be interpreted as a probability.

    Hyperbolic Tangent (tanh): Similar to the sigmoid function, but it squashes the input to a value between -1 and 1:
    tanh⁡(x)=ex−e−xex+e−xtanh(x)=ex+e−xex−e−x​
    Tanh functions are often used in hidden layers of neural networks.

    Rectified Linear Unit (ReLU): ReLU sets all negative values in the input to zero and leaves positive values unchanged:
    f(x)=max⁡(0,x)f(x)=max(0,x)
    ReLU is widely used in deep learning models due to its simplicity and effectiveness in training deep neural networks.

    Leaky ReLU: Leaky ReLU is similar to ReLU but allows a small, positive gradient for negative inputs to prevent dying ReLU problem:
    f(x)={x,if x>0leaky_slope×x,otherwisef(x)={x,leaky_slope×x,​if x>0otherwise​
    where leaky_slopeleaky_slope is a small positive constant.

    Parametric ReLU (PReLU): PReLU is similar to Leaky ReLU but allows the leakage rate to be learned during training rather than being a fixed hyperparameter.

    Exponential Linear Unit (ELU): ELU is a variant of ReLU that smooths the transition for negative inputs:
    f(x)={x,if x>0α×(ex−1),otherwisef(x)={x,α×(ex−1),​if x>0otherwise​
    where αα is a hyperparameter controlling the negative slope for x<0x<0.

    Softmax: Softmax function is used in the output layer for multi-class classification tasks. It converts raw scores into probabilities:
    softmax(xi)=exi∑j=1Nexjsoftmax(xi​)=∑j=1N​exj​exi​​
    where NN is the number of classes.
