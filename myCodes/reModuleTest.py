import re

# rを付けることを推奨。
# バックスラッシュをそのままで分かりやすいため。
content = r'hellow python, 123, end.'
pattern = 'hel'

result = re.match(pattern, content)

if result:  # none以外の場合

    print(result)
    # output:<_sre.SRE_Match object; span=(0, 3), match='hel'>
    print(result.span())
    # output:(0, 3)
    print(result.group())
    # output:hel
