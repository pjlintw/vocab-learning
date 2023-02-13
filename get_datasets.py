import os
import datasets

from m2d2_split_names import M2D2_SPLIT_NAMES

def write_sentence_file(data, file_name, split_name):
    with open(file_name, "w") as wf:
        for line in data[split_name]:
            wf.write(line["text"].strip()+"\n")
    print(f"done: {file_name}")

def main():
    save_dir = "/local/pinjie/m2d2/data"
    fail_downloads = list()
    erros = list()

    # wf = open("record.txt", "w")
    skip_splits = ["eval_sets", "only_text", "only_txt2"]
    # astro-ph.GA  math.CO
    remind_domains = ['astro-ph']

    for domain in remind_domains:
    # for domain in remind_domains:
        if 3==3:
            data = datasets.load_dataset("machelreid/m2d2", domain)
            domain_dir = f"{save_dir}/{domain.lower()}"
            print(data)
            if not os.path.exists(domain_dir):
                os.makedirs(domain_dir)
            # validation
            for file_prefix, split_name in zip(["train","valid","test"], ["train", "validation", "test"]):
                file_name = f"{domain_dir}/{file_prefix}.txt" 
                write_sentence_file(data, file_name, split_name)

            # record the number of data
            #train_size = len(data["train"])
            #valid_size = len(data["validation"])
            #test_size =  len(data["test"])
            #wf.write(f"{domain.lower()},{train_size},{valid_size},{test_size}\n")
            break
        else:
            e = "error"
            fail_downloads.append(domain)
            erros.append(str(e))
    print(f"number of splits: {len(M2D2_SPLIT_NAMES)}")
    print(f"fail to download: {fail_downloads}")
    print(f"erros: {erros}")

    # wf.close()
    #domain = "Health_and_fitness"
    #domain = "cs.CL"
    #data = datasets.load_dataset("machelreid/m2d2", domain)





if __name__ == "__main__":
    main()
