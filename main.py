from engine import Value
from nn import MLP


xs = [[2.0, 3.0, -1.0], 
      [3.0, -1.0, 0.5], 
      [0.5, 1.0, 1.0], 
      [1.0, 1.0, -1.0]]  

ys = [0.0, 1.0, 1.0, 0.0]  


n = MLP(3, [4, 4, 1])


for k in range(20):
    
    ypred = [n(x) for x in xs]
    # Calculate loss as a Value object
    loss = sum((yout - ygt) ** 2 for ygt, yout in zip(ys, ypred))

    # Backward pass
    for p in n.parameters():
        p.grad = 0.0
    loss.backward()  # All of the gradients are accumulated and start from zero

    # Update weights
    for p in n.parameters():
        p.data += -0.1 * p.grad 

    print(k, loss.data)
