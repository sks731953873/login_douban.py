import re

html='''               <td valign="top" colspan="2">
                    <table class="GridViewStyle" cellspacing="0" rules="all" border="1" id="MainWork_dgData" style="border-color:#9CD7FF;width:100%;border-collapse:collapse;">
        <tr class="GridViewHeaderStyle" style="white-space:nowrap;">
                <td>课程</td><td>课程学分</td><td>选修学期</td><td>成绩</td>
        </tr><tr class="GridViewRowStyle">
                <td>高等电磁理论</td><td>3.0</td><td>1</td><td>80</td>
        </tr><tr class="GridViewRowStyle">
                <td>综合英语（一）</td><td>2.0</td><td>1</td><td>81</td>
        </tr><tr class="GridViewRowStyle">
                <td>中国特色社会主义理论与实践研究</td><td>2.0</td><td>1</td><td>86</td>
        </tr>
</table>'''

ptn表=re.compile(r'<table[^>]*?id="MainWork_dgData"[^>]*>.*?</table>',re.S)
ptn行=re.compile(r'<tr[^>]*>.*?</tr>',re.S)
ptn格=re.compile(r'<td[^>]*>(.*?)</td>',re.S)

表=ptn表.findall(html)
行=ptn行.findall(表[0])

格=[]
for td in 行:
    td=ptn格.findall(td)
    格.append(td)
    print(td)
