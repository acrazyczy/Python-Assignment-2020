# int f[421];
# int main() {
# 	int a = 10000;
# 	int b = 0;
# 	int c = 420;
# 	int d = 0;
# 	int e = 0;
# 	int g = 0;

# 	for (;b-c!=0;) 
# 		f[b++] = a/5;
# 	for (;; e = d%a){
# 		d = 0;
# 		g = c*2;
# 		if (g==0) break;
		
# 		for (b=c;;d=d*b){
# 			d=d+f[b]*a;
# 			f[b] = d%--g;
# 			d=d/g--;
# 			if (--b==0) break;
# 		}
		
# 		c = c-14;
# 		printf("%d",e+d/a); // should be printf("%04b"), but let it be
# 	}
	
#   printf("\n");
#   return 0;
# }

def access_f(f, str1, idx, str2, str3):
	f.write(str1 + "if " + idx + " == 0: " + str2 + "f_0" + str3 + "\n")
	for i in range(1, 420):
		f.write(str1 + "elif " + idx + " == " + str(i) + ": " + str2 + "f_" + str(i) + str3 + "\n")
	f.write(str1 + "else: " + str2 + "f_420" + str3 + "\n")

with open("3.in", "w") as f:
	for i in range(421):
		f.write("f_" + str(i) +" = 0\n")
	f.write("a, b, c = 10000, 0, 420\nd, e, g = 0, 0, 0\n")
	f.write("while b - c != 0:\n")
	access_f(f, "\t", "b", "", " = a // 5")
	f.write("\tb += 1\n")
	f.write("while True:\n")
	f.write("\td, g = 0, c * 2\n")
	f.write("\tif g == 0: break\n")
	f.write("\tb = c\n")
	f.write("\twhile True:\n")
	access_f(f, "\t\t", "b", "d = d + ", " * a")
	f.write("\t\tg -= 1\n")
	access_f(f, "\t\t", "b", "", " = d % g")
	f.write("\t\td = d // g\n")
	f.write("\t\tg -= 1\n")
	f.write("\t\tb -= 1\n")
	f.write("\t\tif b == 0: break\n")
	f.write("\t\td *= b\n")
	f.write("\tc -= 14\n")
	f.write("\tprint(e + d // a)\n")
	f.write("\te = d % a\n")