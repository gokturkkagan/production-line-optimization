


from gurobipy import GRB,Model,quicksum #*


def Output(m):  
   
    status_code = {1:'LOADED', 2:'OPTIMAL', 3:'INFEASIBLE', 4:'INF_OR_UNBD', 5:'UNBOUNDED'}  
                                                                                            
    status = m.status
    
    print('The optimization status is ' + status_code[status])
    if status == 2:    
       
        print('Optimal solution:')
        for v in m.getVars():
            print(str(v.varName) + " = " + str(v.x))    
        print('Optimal objective value: ' + str(m.objVal) + "\n")
        
        
def ModelBetterImplemented(c):
 
    model = Model('staj')
    
    
    model.setParam('OutputFlag',True)
    
    n = len(c)
    m=4
   
 
       
    x = model.addVars(n, m, lb=0, ub=GRB.INFINITY, vtype=GRB.BINARY, 
                      name=["x_"+str(i+1)+","+str(j+1) for i in range (n) for j in range(m)]) 
   
    y = model.addVar(vtype=GRB.CONTINUOUS, name="Y")
    model.setObjective(y,GRB.MINIMIZE)
       
    #model.setObjective( quicksum(x[i,1]*c[i]+x[i,2]*c[i]-x[i,3]*c[i]-x[i,4]*c[i] for i in range (25)), GRB.MINIMIZE)
  
    #model.setObjective(y,GRB.MINIMIZE())
   
       
    
    model.addConstr(x[0,0] + x[0,2] == 1, "COM")
    model.addConstr(x[0,1] + x[0,3] == 0, "COM")
    model.addConstr(x[1,0] + x[1,2] == 0, "COM")
    model.addConstr(x[1,1] + x[1,3] == 1, "COM")
    model.addConstr(x[2,0] + x[2,2] == 0, "COM")
    model.addConstr(x[2,1] + x[2,3] == 1, "COM")
    model.addConstr(x[3,0] + x[3,2] == 1, "COM")
    model.addConstr(x[3,1] + x[3,3] == 0, "COM")
    model.addConstr(x[4,0] + x[4,2] == 0, "COM")
    model.addConstr(x[4,1] + x[4,3] == 1, "COM")
    model.addConstr(x[5,0] + x[5,2] == 1, "COM")
    model.addConstr(x[5,1] + x[5,3] == 0, "COM")
    model.addConstr(x[6,0] + x[6,2] == 1, "COM")
    model.addConstr(x[6,1] + x[6,3] == 0, "COM")
    model.addConstr(x[7,0] + x[7,2] == 0, "COM")
    model.addConstr(x[7,1] + x[7,3] == 1, "COM")
    model.addConstr(x[8,0] + x[8,2] == 1, "COM")
    model.addConstr(x[8,1] + x[8,3] == 0, "COM")
    model.addConstr(x[9,0] + x[9,2] == 0, "COM")
    model.addConstr(x[9,1] + x[9,3] == 1, "COM")
    model.addConstr(x[10,0] + x[10,2] == 1, "COM")
    model.addConstr(x[10,1] + x[10,3] == 0, "COM")
    model.addConstr(x[11,0] + x[11,2] == 1, "COM")
    model.addConstr(x[11,1] + x[11,3] == 0, "COM")
    model.addConstr(x[12,0] + x[12,2] == 0, "COM")
    model.addConstr(x[12,1] + x[12,3] == 1, "COM")
    model.addConstr(x[13,0] + x[13,2] == 0, "COM")
    model.addConstr(x[13,1] + x[13,3] == 1, "COM")
    model.addConstr(x[14,0] + x[14,2] == 1, "COM")
    model.addConstr(x[14,1] + x[14,3] == 0, "COM")
    model.addConstr(x[15,0] + x[15,2] == 1, "COM")
    model.addConstr(x[15,1] + x[15,3] == 0, "COM")
    model.addConstr(x[16,0] + x[16,2] == 0, "COM")
    model.addConstr(x[16,1] + x[16,3] == 1, "COM")
    model.addConstr(x[17,0] + x[17,2] == 0, "COM")
    model.addConstr(x[17,1] + x[17,3] == 1, "COM")
    model.addConstr(x[18,0] + x[18,2] == 0, "COM")
    model.addConstr(x[18,1] + x[18,3] == 1, "COM")
    model.addConstr(x[19,0] + x[19,2] == 1, "COM")
    model.addConstr(x[19,1] + x[19,3] == 0, "COM")
    model.addConstr(x[20,0] + x[20,2] == 1, "COM")
    model.addConstr(x[20,1] + x[20,3] == 0, "COM")
    model.addConstr(x[21,0] + x[21,2] == 0, "COM")
    model.addConstr(x[21,1] + x[21,3] == 1, "COM")
    model.addConstr(x[22,0] + x[22,2] == 0, "COM")
    model.addConstr(x[22,1] + x[22,3] == 1, "COM")
    model.addConstr(x[23,0] + x[23,2] == 1, "COM")
    model.addConstr(x[23,1] + x[23,3] == 0, "COM")
    model.addConstr(x[24,0] + x[24,2] == 1, "COM")
    model.addConstr(x[24,1] + x[24,3] == 0, "COM")
   
    

    
    model.addConstr(quicksum(x[i,0]*c[i]+x[i,1]*c[i]-x[i,2]*c[i]-x[i,3]*c[i] for i in range (25))<=y)
                
    
                
    model.addConstr(quicksum(-x[i,0]*c[i]-x[i,1]*c[i]+x[i,2]*c[i]+x[i,3]*c[i] for i in range (25))<=y)
    
    
    
    model.optimize()
    
    Output(model)
    
  
    model.write('staj.lp')
    

    model.write('staj.sol')
  
                    
                
                    
            
    

ModelBetterImplemented(c=[5.2,5.1,19.2,7.7,0,0,5.2,7.1,7.5,0,3.8,4.7,6.8,13.7,11.3,17.2,17.2,7.6,11.4,0,7.8,0,8.2,0,0]
                    )