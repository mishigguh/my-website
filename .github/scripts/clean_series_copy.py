from pathlib import Path
p=Path('bodywork.html')
t=p.read_text()
t=t.replace('The series is $435 and begins with a 75-minute bodywork session. Once the dedicated Acuity series appointment is created, this button will take you directly to that checkout and first-session calendar.','The series is $435 and begins with a 75-minute bodywork session. Choose your first appointment through the secure scheduler; we arrange the remaining sessions together after the first visit.')
t=t.replace('<p class="microcopy" style="margin-top:1rem">The current button opens my secure Acuity scheduler. A direct series checkout link will replace it once that appointment type is created.</p>','<!-- TODO before merge: replace the current scheduler href with the dedicated Acuity series appointment URL once that appointment type exists. -->')
t=t.replace('Do I have to buy the four-session process?','Do I have to buy the four-session series?')
t=t.replace('The four-session process is simply the starting point I recommend','The four-session series is simply the starting point I recommend')
p.write_text(t)
