import random
import matplotlib.pyplot as plt
  
n = 10000
  
circle_points= 0
square_points= 0
pi_list = []
  
for i in range(n):
  
    rand_x= random.uniform(0, 1)
    rand_y= random.uniform(0, 1)
  
    origin_dist= rand_x**2 + rand_y**2
  
    if origin_dist<= 1:
        circle_points+= 1
        plt.plot(rand_x , rand_y , 'g.') 
        
    else:
        plt.plot(rand_x , rand_y , 'r.')
    
    square_points+= 1
    

    # pi= 4*(numb of points generated inside the circle)/ (numb of points generated inside the square)
    pi = 4* circle_points/ square_points
    pi_list.append(pi)
  
 
print("Final Estimation of Pi=", pi)    
plt.show()
plt.plot(pi_list)
plt.title('Estimation of Pi value with MC method')
plt.show()