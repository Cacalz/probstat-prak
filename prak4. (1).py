#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# Fungsi untuk menghasilkan sampel dari distribusi eksponensial
def generate_exponential_samples(lamda, size):
    return np.random.exponential(scale=1/lamda, size=size)

# Parameter distribusi (tingkat parameter lamda)
lamda = 0.5  # Tingkat kedatangan peristiwa per satuan waktu

# Jumlah peristiwa yang akan diamati
num_events = 1000

# Generate sampel waktu antara kedatangan dua peristiwa
interarrival_times = generate_exponential_samples(lamda, num_events)

# Mencetak waktu antara kedatangan dua peristiwa pertama lima peristiwa
print("Waktu Antara Kedatangan Peristiwa Pertama Lima Peristiwa:")
for i in range(5):
    print("Peristiwa", i+1, ": ", interarrival_times[i])

# Mencetak rata-rata waktu antara kedatangan dua peristiwa
mean_interarrival_time = np.mean(interarrival_times)
print("\nRata-rata Waktu Antara Kedatangan Peristiwa:", mean_interarrival_time)

# Mencetak jumlah peristiwa yang terjadi dalam 10 satuan waktu
time_interval = 10
num_events_in_interval = np.sum(interarrival_times <= time_interval)
print("\nJumlah Peristiwa yang Terjadi dalam", time_interval, "Satuan Waktu:", num_events_in_interval)

print("\nJumlah Peristiwa dalam Interval Waktu {} satuan: {}".format(time_interval, num_events_in_interval))


# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan sampel dari distribusi eksponensial
def generate_exponential_samples(lamda, size):
    return np.random.exponential(scale=1/lamda, size=size)

# Parameter distribusi (tingkat parameter lamda)
lamda = 1/10  # Rata-rata waktu kedatangan pelanggan adalah 10 menit

# Waktu yang diberikan (dalam menit)
time_interval = 30

# Jumlah sampel yang akan digunakan
num_samples = 10000

# Generate sampel waktu antara kedatangan pelanggan
interarrival_times = generate_exponential_samples(lamda, num_samples)

# Hitung berapa banyak pelanggan yang diharapkan tiba dalam interval waktu yang diberikan
num_arrivals_in_interval = np.sum(interarrival_times <= time_interval)
print("Jumlah pelanggan yang diharapkan tiba pada pukul 11:30 pagi:", num_arrivals_in_interval)

# Plot histogram dari sampel waktu antara kedatangan pelanggan
plt.hist(interarrival_times, bins=30, density=True, alpha=0.6, color='g')
plt.xlabel('Waktu Antara Kedatangan Pelanggan (menit)')
plt.ylabel('Frekuensi')
plt.title('Histogram Waktu Antara Kedatangan Pelanggan')
plt.grid(True)
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan sampel dari distribusi Weibull
def generate_weibull_samples(shape, scale, size):
    return np.random.weibull(shape, size) * scale

# Parameter distribusi Weibull
shape = 2.0  # parameter bentuk
scale = 1.0  # parameter skala

# Jumlah sampel yang akan dihasilkan
sample_size = 1000

# Generate sampel dari distribusi Weibull
samples = generate_weibull_samples(shape, scale, sample_size)

# Plot histogram dari sampel
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

# Label sumbu
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

# Judul plot
plt.title('Distribusi Weibull dengan Parameter Shape={} dan Scale={}'.format(shape, scale))

# Tampilkan grid
plt.grid(True)

# Tampilkan plot
plt.show()


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parameter distribusi Weibull
shape = 1.8  # parameter bentuk
scale = 5  # parameter skala (dalam tahun)

# Waktu yang diberikan (dalam tahun)
time_threshold = 3

# Menghitung persentase produk yang diharapkan bertahan selama setidaknya 3 tahun
percentage_survival = (1 - weibull_min.cdf(time_threshold, shape, scale=scale)) * 100

print("Persentase produk yang diharapkan bertahan selama setidaknya 3 tahun:", percentage_survival, "%")

# Plot PDF (Probability Density Function) distribusi Weibull
x = np.linspace(0, 10, 1000)  # rentang hingga 10 tahun
pdf = weibull_min.pdf(x, shape, scale=scale)
plt.plot(x, pdf, 'r', linewidth=2)

# Label sumbu
plt.xlabel('Masa Pakai (tahun)')
plt.ylabel('Densitas')

# Judul plot
plt.title('Distribusi Weibull dengan Parameter Shape={} dan Scale={}'.format(shape, scale))

# Tampilkan grid
plt.grid(True)

# Tampilkan plot
plt.show()


# In[19]:


import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan sampel dari distribusi eksponensial
def generate_exponential_samples(lamda, size):
    return np.random.exponential(scale=1/lamda, size=size)

# Parameter distribusi (tingkat parameter lamda)
lamda = 1/18  # Rata-rata waktu kedatangan pelanggan adalah 18 menit

# Waktu yang diberikan (dalam menit)
time_interval = 2 * 60  

# Jumlah sampel yang akan digunakan
num_samples = 10000

# Generate sampel waktu antara kedatangan pelanggan
interarrival_times = generate_exponential_samples(lamda, num_samples)

# Hitung berapa banyak pelanggan yang diharapkan tiba dalam interval waktu yang diberikan
num_arrivals_in_interval = np.sum(interarrival_times <= time_interval)
print("Jumlah pelanggan yang diharapkan tiba pada pukul 9:", num_arrivals_in_interval)

# Plot histogram dari sampel waktu antara kedatangan pelanggan
plt.hist(interarrival_times, bins=30, density=True, alpha=0.6, color='g')
plt.xlabel('Waktu Antara Kedatangan Pelanggan (menit)')
plt.ylabel('Frekuensi')
plt.title('Histogram Waktu Antara Kedatangan Pelanggan')
plt.grid(True)
plt.show()


# In[25]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# Parameter distribusi Weibull
shape = 1.8  # parameter bentuk
scale = 5  # parameter skala (dalam tahun)

# Waktu yang diberikan (dalam tahun)
time_threshold = 11

# Menghitung persentase produk yang diharapkan bertahan selama setidaknya (3+8) tahun
percentage_survival = (1 - weibull_min.cdf(time_threshold, shape, scale=scale)) * 500

print("Persentase produk yang diharapkan bertahan selama setidaknya 11 tahun:", percentage_survival, "%")

# Plot PDF (Probability Density Function) distribusi Weibull
x = np.linspace(0, 10, 1000)  # rentang hingga 20 tahun
pdf = weibull_min.pdf(x, shape, scale=scale)
plt.plot(x, pdf, 'r', linewidth=2)

# Label sumbu
plt.xlabel('Masa Pakai (tahun)')
plt.ylabel('Densitas')

# Judul plot
plt.title('Distribusi Weibull dengan Parameter Shape={} dan Scale={}'.format(shape, scale))

# Tampilkan grid
plt.grid(True)

# Tampilkan plot
plt.show()


# In[ ]:




