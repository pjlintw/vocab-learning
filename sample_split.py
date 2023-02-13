import os
import random
from random import Random

MAPPING = {
        "Health_and_fitness": [],
        "History_and_events": [],
        "Society_and_social_sciences": [],
        "Technology_and_applied_sciences": [],
        "Culture_and_the_arts": [],
        "Natural_and_physical_sciences": [], 
        "Human_activaites": [],
        "Mathematics_and_logic": [],
        "General_reference": [],
        "Religion_and_belief_systems": [],
        "Philosophy_and_thinking": [],

        "Mathematics": "math",
        "Quantitative_biology": "q-bio",
        "Physics": "physics",
        "Nonlinear_sciences": "nlin",
        "Condensed_matter": "cond-mat",
        "Economics": "econ",
        "Computer_sciences": "cs",
        "Statistics": "stat",
        "Astrophysic": "astro",
        "Art": "",
        "Philosophy": ""
}

# 原始命名檔案有錯誤
# general reference
# human activ
wiki_domains = {"health_and_fitness", "history_and_events",
               "society_and_social_sciences", "technology_and_applied_sciences",
               "culture_and_the_arts", "natural_and_physical_sciences",
               "human_activities", "mathematics_and_logic",
               "general_reference", "religion_and_belief_systems",
                "philosophy_and_thinking"}


s2orc_domains = ["math", "q-bio", "physics", "nlin", "cond-mat", "econ", "cs", "stat", "astro", "art", "philosophy"]



def split_integer(total_size, k):
    quotient = int(total_size/k)
    remainder = total_size % k
    if remainder > 0:
        return [quotient] * (k - remainder) + [quotient + 1] * remainder
    if remainder < 0:
        return [quotient-1] * -remainder + [quotient] * (k + remainder)
    return [quotient] * k

def read_file(fname):
    with open(fname, "r") as f:
        data = f.readlines()
    data = [ line.strip() for line in data if line != "\n" ]
    return data 


def write_file(fname, sentences):
    """
    fname: file name
    sentences: list of sentences
    """
    with open(fname, "w") as wf:
        for sent in sentences:
            wf.write(sent.strip()+"\n")


def sample_k_from_split(domain_dir, domain_name, split_name, k, rand): 
    random_sentences = list()
    if domain_name == "wiki":
        # List of sentences
        sample_pool = read_file(f"{domain_dir}/{split_name}.txt")
        random_k = rand.sample(sample_pool, k=k)

    elif domain_name == "s2orc":
        # List of sentences
        sample_pool = read_file(f"{domain_dir}/{split_name}.txt")    
        random_k = rand.sample(sample_pool, k=k)
    return random_k


def create_dir(directories):
    if not os.path.exists(directories):
        os.makedirs(directories)

def write_test_set_from_sampled_domain(test_wf,
                                       sampled_wiki_domains,
                                       sampled_s2orc_domains,
                                       wiki_sample_sizes,
                                       s2orc_sample_sizes,
                                       rand):

    test_dir_prefix = "m2d2_test_sets"
    for d, k in zip(sampled_wiki_domains, wiki_sample_sizes):
        # typo handeling
        if d == "human_activities":
            d = "Human_activites"
        elif d == "general_reference":
            d = "General_referece"
        else:
            d = d.capitalize()
        d = [ domain for domain in os.listdir(test_dir_prefix+"/wikipedia") if domain.lower() == d.lower() ][0]
        sample_pool = read_file(os.path.join(f"{test_dir_prefix}/wikipedia/{d}/test.txt"))
        random_k = rand.sample(sample_pool, k=k)
        [test_wf.write(line.strip()+"\n") for line in random_k]

    for d, k in zip(sampled_s2orc_domains, s2orc_sample_sizes):
        d = [ domain for domain in os.listdir(test_dir_prefix+"/s2orc") if domain.lower() == d.lower() ][0]
        sample_pool = read_file(os.path.join(f"{test_dir_prefix}/s2orc/{d}/test.txt"))
        random_k = rand.sample(sample_pool, k=k)
        [test_wf.write(line.strip()+"\n") for line in random_k]


def main():
    
    total_size = 10000
    num_domains = 22
    print(split_integer(total_size, num_domains))
    
    # s2orc
    s2orc_test_dir = "m2d2_test_sets/s2orc/"
    s2orc_test_domains = [ d.lower() for d in os.listdir(s2orc_test_dir)]
    # wikipedia
    wiki_test_dir = "m2d2_test_sets/wikipedia/"
    wiki_test_domains = [ d.lower() for d in os.listdir(wiki_test_dir)]
    
    # 重新命名 typo 檔案
    wiki_test_domains = [ d.replace("activites", "activities").replace("referece", "reference") for d in wiki_test_domains]
    print(s2orc_test_domains)
    print(wiki_test_domains)

    print(s2orc_domains)

    # s2orc:
    s2orc_match_domains = [ d for d in s2orc_test_domains for d_prefix in s2orc_domains if d.startswith(d_prefix)]
    #print(s2orc_match_domains)    

    # wiki domains
    wiki_match_domains = [ d for d in wiki_test_domains for d_prefix in wiki_domains if d == (d_prefix)]
    #print(match_domains)
    #print(len(match_domains))

    # data dir: resource
    data_dir = "/local/pinjie/m2d2/data"
    # target dir
    save_dir_prefix = "/local/pinjie/m2d2/md_data"

    size2str = {100: "sample_100",
                10000: "sample_10k_copy2",
                20000: "sample_20k",
                30000: "sample_30k",
                50000: "sample_50k"}

    # 1k - train.split
    for num_size in [30000, 50000]:     
        sizes = split_integer(num_size, 22)
        dev_sizes = split_integer(8000, 22)
        assert sum(sizes) == num_size
        print(sizes)
        print(sum(sizes))
        # 分配大小
        #print(sizes)
        #print(dev_sizes)
        wiki_sizes = sizes[:11]
        s2orc_sizes = sizes[11:]

        wiki_dev_sizes = dev_sizes[:11]
        s2orc_dev_sizes = dev_sizes[11:]

        assert len(wiki_sizes)+len(s2orc_sizes) == 22
        assert  len(wiki_dev_sizes)+len(s2orc_dev_sizes) == 22
        domain_idx = 0

        # 123, 1234, 33, 34, 32, 31,30,
        # random.seed(34)
        rand = Random(41)

        # create sample_10k folder
        sampled_dir = os.path.join(save_dir_prefix, size2str[num_size])
        create_dir(sampled_dir)
        train_wf = open(f"{sampled_dir}/train.txt", "w")
        valid_wf = open(f"{sampled_dir}/valid.txt", "w")
        test_wf = open(f"{sampled_dir}/test.txt", "w")

        sampled_wiki_domains = list()
        sampled_s2orc_domains = list()

        ### wiki ### 
        for idx in range(len(wiki_match_domains)):
            num_random_size = wiki_sizes[idx]
            num_dev_size = wiki_dev_sizes[idx]
            d_folder = wiki_match_domains[idx]

            sampled_wiki_domains.append(d_folder)
            # path
            domain_dir = os.path.join(data_dir, d_folder)
            print("sample from:", domain_dir)
            
            ### sample ###
            sample_k = sample_k_from_split(domain_dir,
                                           "wiki",
                                           "train",
                                           num_random_size,
                                           rand)
            print("num_random_size", num_random_size)
            print("sample k (len)", len(sample_k))
            for line in sample_k:
                train_wf.write(line.strip()+"\n") 
            assert len(sample_k) == num_random_size 
            # create save dir
            save_dir = os.path.join(save_dir_prefix, size2str[num_size], f"{domain_idx}_{d_folder.lower()}")
            create_dir(save_dir)
            split_name = os.path.join(save_dir, "train.txt")
            write_file(split_name, sample_k)
            print("save to (train):", save_dir)
            
            ### sample dev ###
            sample_k = sample_k_from_split(domain_dir,
                                           "wiki",
                                           "valid",
                                           num_dev_size,
                                           rand)
            [ valid_wf.write(line.strip()+"\n") for line in sample_k ]
            assert len(sample_k) == num_dev_size
            # create save dir
            split_name = os.path.join(save_dir, "valid.txt")
            write_file(split_name, sample_k)
            print("save to (valid):", save_dir)
                        
            domain_idx += 1
        
        ### s2orc ###
        for idx in range(len(s2orc_domains)):
            num_random_size = s2orc_sizes[idx]
            num_dev_size = s2orc_dev_sizes[idx]
            d_folder = s2orc_domains[idx]
            print(d_folder)
            d_folder = rand.choice([ d for d in s2orc_test_domains if d.startswith(d_folder)])
            while d_folder in ["math.it"]:
                d_folder = rand.choice([ d for d in s2orc_test_domains if d.startswith(d_folder)])
                print("new random folder", d_folder)

            # 保證 sample 的 folder 存在
            assert d_folder in s2orc_test_domains
            sampled_s2orc_domains.append(d_folder)

            # path
            domain_dir = os.path.join(data_dir, d_folder)
            print("sample from:", domain_dir)
            
            ### sample ###
            sample_k = sample_k_from_split(domain_dir,
                                           "s2orc",
                                           "train",
                                           num_random_size,
                                           rand)
            for line in sample_k:
                train_wf.write(line.strip()+"\n")
            print("num_random_size", num_random_size)
            print("sample k (len)", len(sample_k))
            assert len(sample_k) == num_random_size 
            # create save dir
            save_dir = os.path.join(save_dir_prefix, size2str[num_size], f"{domain_idx}_{d_folder.lower()}")
            create_dir(save_dir)
            split_name = os.path.join(save_dir, "train.txt")
            write_file(split_name, sample_k)
            print("save to (train):", save_dir)
            
            ### sample dev ###
            sample_k = sample_k_from_split(domain_dir,
                                           "s2orc",
                                           "valid",
                                           num_dev_size,
                                           rand)
            [ valid_wf.write(line.strip()+"\n") for line in sample_k ]
            assert len(sample_k) == num_dev_size
            # create save dir
            split_name = os.path.join(save_dir, "valid.txt")
            write_file(split_name, sample_k)
            print("save to (valid):", save_dir)

            domain_idx += 1
            
        train_wf.close()
        valid_wf.close()
        write_test_set_from_sampled_domain(test_wf,
                                           sampled_wiki_domains,
                                           sampled_s2orc_domains,
                                           wiki_sample_sizes=wiki_dev_sizes,
                                           s2orc_sample_sizes=s2orc_dev_sizes,
                                           rand=rand)
    return None




if __name__ == "__main__":
    main()
