''' Histogram Plots '''
#
# plt.figure(1)
# count, bins, ignored = plt.hist(s, bin_amount, normed=True)
# gaussian = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2))
# plt.xlabel(r'$B$ [$Gauss$]')
# plt.ylabel(r'# plt$H_0$')
# plt.title(r'$H_0$ Histogram')
# plt.savefig(fname1)
# plt.show(block=True)
#
# plt.figure(2)
# count, bins, ignored = plt.hist(h_tot(s), bin_amount, normed=True)
# plt.xlabel(r'$B$ [$Gauss$]')
# plt.ylabel(r'# $H_{tot}$')
# plt.title(r'$H_{tot}$ Histogram')
# plt.savefig(fname2)
# plt.show(block=True)


''' Plots '''

# fig = plt.figure(3)
# plt.plot(t,signal_array)
# plt.xlabel(r'$t$ $[s]$')
# plt.ylabel(r'$\overline{S_z}(H_0))$ $[]$')
# #np.plt.title(r'Average Polarization Signal - $\omega$ = {}'.format(omega_int))
# fig.tight_layout()
# plt.savefig(fname3)
# plt.show(block=True)

fig = plt.figure(4)
plt.plot(t[a],signal_array[a],'.')
plt.xlabel(r'$t$ $[s]$')
plt.ylabel(r'Amplitude $\overline{S_z}(H_0))$ $[]$')
#np.plt.title(r'Average Polarization Signal - $\omega$ = {}'.format(omega_int))
fig.tight_layout()
plt.savefig(fname4)
plt.show(block=True)
