The different folders refer to different campaigns, and then there is a "duplicates" folder that contains concatenated data for multi campaign targets.

For most stars, there is a weighted and an un-weighted PDS. Results from average seismic parameters comes from the un-weighted PDS (*check for exceptions*). In a few cases the weigthed spectrum looks a bit strange from a bad integration of the window function, so the un-weighted spectra are generally better to use.

And, as you know, the systematics in the K2 data is a pain and many stars will have some residual at the know integer values of ~47uHz.

For many campaigns, the apertures were defined by hand, but for some, typically for the fainter un-saturated stars, the apertures were defined automatically by the k2p2 routine - in these cases, there may be additional stars identified in the frame, which in their names will have been identified as "_02", "_03", etc. - the main target to be concerned about is the one with "_01" in the filenames.

Departures from the above:
For the C10 target EPIC 228775782, a detection was made based on the weighted PDS only.

For C11 there are two sub-parts, C11.1-C11.2, where only the time series are provided. I made PDS from combined sub-parts in C11_combined.

In C16 the main target associated with EPIC 211408138 is the "_02" target file!.

For the "dublicate" targets there are six psd per target, using different combinations of weighting. The psd_tot files, using the concatenated time series, have 4 columns, with two sets of (frequency, power), the first set being unweighted the second being weighted. The unweighted spectra were used for the average analysis.

In addition to this, there is a "psd_av" file containing averaged spectra, with different combinations of weighting. The first column is frequency, the following 4 are different versions of the averaged power (we could call them r1-r4). Average results from these were obtained from r2 (column 2).
