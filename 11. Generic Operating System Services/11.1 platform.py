"""
@file: 11.1 platform.py
@time: 2019/01/23
@author: sch
"""
import platform

print("platform.platform() -> ", platform.platform())
print("platform.architecture() -> ", platform.architecture())

print("\nplatform.uname() -> ", platform.uname())
print("platform.system() -> ", platform.system())
print("platform.node() -> ", platform.node())
print("platform.release() -> ", platform.release())
print("platform.version() -> ", platform.version())
print("platform.machine() -> ", platform.machine())
print("platform.processor() -> ", platform.processor())

print("\nplatform.libc_ver() -> ", platform.libc_ver())
print("platform.linux_distribution() -> ", platform.linux_distribution())
print("platform.dist() -> ", platform.dist())
print("platform.popen(\"ls - l\").read() -> ", platform.popen("ls -l").read())

print("\nplatform.python_version() -> ", platform.python_version())
print("platform.python_version_tuple() -> ", platform.python_version_tuple())
print("platform.python_branch() -> ", platform.python_branch())
print("platform.python_build() -> ", platform.python_build())
print("platform.python_compiler() -> ", platform.python_compiler())
print("platform.python_implementation() -> ", platform.python_implementation())
print("platform.python_revision() -> ", platform.python_revision())

print(platform.java_ver())

print("\nplatform.mac_ver() -> ", platform.mac_ver())
print("platform.win32_ver() -> ", platform.win32_ver())

print("\nplatform.system_alias(platform.system(), platform.release(), platform.version()) -> ", platform.system_alias(platform.system(), platform.release(), platform.version()))
print("platform.machine() -> ", platform.machine())
print("platform.processor() -> ", platform.processor())
