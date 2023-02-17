# Método de Euler-Cromer:   
for i in range(0, t.size-1):
    rr = np.sqrt(Rx[i]**2 + Ry[i]**2)
    ax[i] = -g*m/rr**3*Rx[i]
    ay[i] = -g*m/rr**3*Ry[i]
    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    Rx[i+1] = Rx[i] + vx[i+1]*dt
    Ry[i+1] = Ry[i] + vy[i+1]*dt