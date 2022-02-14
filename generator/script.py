# %%

import pandas as pd
import os
import shutil
import glob

csv_path = "https://docs.google.com/spreadsheets/d/1DaVZe8kC2-SQNaHKkguJQhgt00epRxUC-1Q-3KQ205c"
extension = "/export?gid=1894787571&format=csv"
df = pd.read_csv(csv_path + extension, keep_default_na=False)

base_url = "../_projects/"
for i, row in df.iterrows():
    project_name = row['name']
    if os.path.isdir(base_url + project_name):
        shutil.rmtree(base_url + project_name)
    if not os.path.isdir(base_url + project_name):
        os.mkdir(base_url + project_name)

        index_file = os.path.join(base_url, project_name, "index.md")
        if not os.path.isfile(index_file):
            with open(index_file, 'w') as f:
                f.write('---')
                f.write('\n')
                if not not row['date']:
                    f.write('date: ' + row['date'])
                    f.write('\n')
                if not not row['title']:
                    f.write('title: ' + row['title'])
                    f.write('\n')
                if not not row['keywords']:
                    f.write('tags: ' + '[' + ','.join(row['keywords'].split(';')[:-1]) + ']')
                    f.write('\n')
                # if not not row['keywords']:
                #     f.write('keywords: ' + row['keywords'])
                #     f.write('\n')
                if not not row['technologies']:
                    f.write('technologies: ' + row['technologies'])
                    f.write('\n')
                if not not row['description']:
                    f.write('description: ' + row['description'])
                    f.write('\n')
                if True: #not not row['img']:
                    extensions = ["png","jpeg","jpg","gif"]
                    images = []
                    for ext in extensions:
                        images.extend(glob.glob("./figures/"+ project_name + "*." + ext))
                    img = os.path.basename(images[0])
                    
                    if not not row['thumbnail']:
                        images = glob.glob("./figures/"+ project_name + row['thumbnail'] + "*")
                        img = os.path.basename(images[0])
                    f.write('thumbnail: ' + img)
                    f.write('\n')
                if True: #not not row['img']:
                    extensions = ["png","jpeg","jpg","gif"]
                    images = []
                    for ext in extensions:
                        images.extend(glob.glob("./figures/"+ project_name + "*." + ext))
                    img = os.path.basename(images[0])
                    
                    if not not row['img']:
                        images = glob.glob("./figures/"+ project_name + row['img'] + "*")
                        img = os.path.basename(images[0])
                    f.write('img: ' + img)
                    f.write('\n')
                if not not row['link']:
                    f.write('link: ' + row['link'])
                    f.write('\n')
                if not not row['github']:
                    f.write('github: ' + row['github'])
                    f.write('\n')
                if not not row['featured']:
                    f.write('featured: ' + str(row['featured']))
                    f.write('\n')
                f.write('---')
                f.write('\n')
                if not not row['content']:
                    f.write('\n')
                    f.write(row['content'])
                    f.write('\n')

        images = glob.glob("./figures/"+ project_name + "*")
        for img in images:
            shutil.copyfile(img, base_url + project_name + "/" + os.path.basename(img))

print(os.getcwd())