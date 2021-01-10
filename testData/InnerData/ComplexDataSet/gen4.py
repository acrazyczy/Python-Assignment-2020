# int a[233];
# int n = 233;

# int qsrt(int l, int r) {
#     int i = l;
#     int j = r;
#     int x = a[(l + r) / 2];
#     while (i <= j) {
#         while (a[i] < x) i++;
#         while (a[j] > x) j--;
#         if (i <= j) {
#             int temp = a[i];
#             a[i] = a[j];
#             a[j] = temp;
#             i++;
#             j--;
#         }
#     }
#     if (l < j) qsrt(l, j);
#     if (i < r) qsrt(i, r);
#     return 0;
# }

# int main() {
#     int i;
#     for (i = 0; i < n; i++)
#         a[i] = n - 1 - i;
#     qsrt(0, n - 1);
#     for (i = 0; i < n; i++) {
# 		printf("%d\n", a[i]);
# 	}
#     printf("\n");
#     return 0;
# }

n = 233


def access_f(f, str1, idx, str2, str3):
	f.write(str1 + "if " + idx + " == 0: " + str2 + "f_0" + str3 + "\n")
	for i in range(1, n - 1):
		f.write(str1 + "elif " + idx + " == " + str(i) + ": " + str2 + "f_" + str(i) + str3 + "\n")
	f.write(str1 + "else: " + str2 + "f_" + str(n - 1) + str3 + "\n")

with open("4.in", "w") as f:
	f.write("n = " + str(n) + "\n")
	for i in range(n):
		f.write("f_" + str(i) + " = " + str(n - 1 - i) + "\n")
	f.write("\n\ndef qsort(l, r):\n")
	f.write("\ti, j, x = l, r, 0\n")
	access_f(f, "\t", "(l + r) // 2", "x = ", "")
	f.write("\twhile i <= j:\n")
	f.write("\t\twhile True:\n")
	f.write("\t\t\ttmp = 0\n")
	access_f(f, "\t\t\t", "i", "tmp = ", "")
	f.write("\t\t\tif tmp >= x: break\n")
	f.write("\t\t\ti += 1\n")
	f.write("\t\twhile True:\n")
	f.write("\t\t\ttmp = 0\n")
	access_f(f, "\t\t\t", "j", "tmp = ", "")
	f.write("\t\t\tif tmp <= x: break\n")
	f.write("\t\t\tj -= 1\n")
	f.write("\t\tif i <= j:\n")
	f.write("\t\t\ttmpi, tmpj = 0, 0\n")
	access_f(f, "\t\t\t", "i", "tmpi = ", "")
	access_f(f, "\t\t\t", "j", "tmpj = ", "")
	access_f(f, "\t\t\t", "i", "", " = tmpj")
	access_f(f, "\t\t\t", "j", "", " = tmpi")
	f.write("\t\t\ti += 1\n")
	f.write("\t\t\tj -= 1\n")
	f.write("\tif l < j: qsort(l, j)\n")
	f.write("\tif i < r: qsort(i, r)\n\n\n")
	f.write("qsort(0, n - 1)\n")
	f.write("k = 0\n")
	f.write("while k < n:\n")
	access_f(f, "\t", "k", "print(", ")")
	f.write("\tk += 1\n")