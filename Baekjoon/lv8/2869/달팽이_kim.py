#메모리 33376kb, 시간 44ms
import sys, math
A,B,V = map(int,sys.stdin.readline().split())
oneDayJump = A-B
#낮에 정상에 도달하면 밤에 내려오지 않기 때문에 
#정상에 도달할 수 있는 지점은 올라가는 A기준으로  
breakPoint = V-A
# ans x onedayjump >= breakpoint 을 만족하는 최소 정수 ans에  
#breakpoint에 도달후 올라가는 1일 더하기 
ans = math.ceil(breakPoint/oneDayJump) + 1
print(ans)