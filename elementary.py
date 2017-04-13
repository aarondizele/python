import os, sys, re, subprocess

print("Elementary App work!")

# def List(dir):
#     cmd = 'ls -l ' + dir
#     (status, output) = subprocess.getstatusoutput(cmd)

#     if status:
#         sys.stderr.write('there was an error: '+ output)
#         sys.exit(1)

#     print(output)

# # def List(dir):
# #     filenames = os.listdir(dir)
# #     for filename in filenames:
# #         path = os.path.join(dir, filename)
# #         # print(path)
# #         absoluteVersionOfPath = os.path.abspath(path)
# #         # print(absoluteVersionOfPath)

# # print(os.path.exists('app.exe'))

# def main():
#     List(sys.argv[1])

# if __name__ == '__main__':
#     main()