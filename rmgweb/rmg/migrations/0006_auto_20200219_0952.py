# Generated by Django 2.2.5 on 2020-02-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmg', '0005_auto_20200219_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reactionlibrary',
            name='reaction_lib',
            field=models.CharField(blank=True, choices=[('1989_Stewart_2CH3_to_C2H5_H', '1989_Stewart_2CH3_to_C2H5_H'), ('2001_Tokmakov_H_Toluene_to_CH3_Benzene', '2001_Tokmakov_H_Toluene_to_CH3_Benzene'), ('2003_Miller_Propargyl_Recomb_High_P', '2003_Miller_Propargyl_Recomb_High_P'), ('2005_Senosiain_OH_C2H2', '2005_Senosiain_OH_C2H2'), ('2006_Joshi_OH_CO', '2006_Joshi_OH_CO'), ('2009_Sharma_C5H5_CH3_highP', '2009_Sharma_C5H5_CH3_highP'), ('2015_Buras_C2H3_C4H6_highP', '2015_Buras_C2H3_C4H6_highP'), ('BurkeH2O2inArHe', 'BurkeH2O2inArHe'), ('BurkeH2O2inN2', 'BurkeH2O2inN2'), ('C10H11', 'C10H11'), ('C2H4+O_Klipp2017', 'C2H4+O_Klipp2017'), ('C3', 'C3'), ('C6H5_C4H4_Mebel', 'C6H5_C4H4_Mebel'), ('Chernov', 'Chernov'), ('CurranPentane', 'CurranPentane'), ('DMSOxy', 'DMSOxy'), ('Dooley/C1', 'Dooley/C1'), ('Dooley/methylformate', 'Dooley/methylformate'), ('Dooley/methylformate_2', 'Dooley/methylformate_2'), ('Dooley/methylformate_all_ARHEbathgas', 'Dooley/methylformate_all_ARHEbathgas'), ('Dooley/methylformate_all_N2bathgas', 'Dooley/methylformate_all_N2bathgas'), ('ERC-FoundationFuelv0.9', 'ERC-FoundationFuelv0.9'), ('Ethylamine', 'Ethylamine'), ('FFCM1(-)', 'FFCM1(-)'), ('First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP', 'First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP'), ('First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP', 'First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP'), ('First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP', 'First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP'), ('First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP', 'First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP'), ('First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP', 'First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP'), ('First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP', 'First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP'), ('First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP', 'First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP'), ('First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP', 'First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP'), ('First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP', 'First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP'), ('First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP', 'First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP'), ('First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective', 'First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective'), ('Fulvene_H', 'Fulvene_H'), ('GRI-HCO', 'GRI-HCO'), ('GRI-Mech3.0', 'GRI-Mech3.0'), ('GRI-Mech3.0-N', 'GRI-Mech3.0-N'), ('Glarborg/C0', 'Glarborg/C0'), ('Glarborg/C1', 'Glarborg/C1'), ('Glarborg/C2', 'Glarborg/C2'), ('Glarborg/C3', 'Glarborg/C3'), ('Glarborg/highP', 'Glarborg/highP'), ('HydrazinePDep', 'HydrazinePDep'), ('Iodine-R_recombination', 'Iodine-R_recombination'), ('JetSurF1.0', 'JetSurF1.0'), ('JetSurF2.0', 'JetSurF2.0'), ('Klippenstein_Glarborg2016', 'Klippenstein_Glarborg2016'), ('Lai_Hexylbenzene', 'Lai_Hexylbenzene'), ('Mebel_C6H5_C2H2', 'Mebel_C6H5_C2H2'), ('Mebel_Naphthyl', 'Mebel_Naphthyl'), ('Methylformate', 'Methylformate'), ('N-S_interactions', 'N-S_interactions'), ('NOx2018', 'NOx2018'), ('Narayanaswamy', 'Narayanaswamy'), ('Nitrogen_Dean_and_Bozzelli', 'Nitrogen_Dean_and_Bozzelli'), ('Nitrogen_Glarborg_Gimenez_et_al', 'Nitrogen_Glarborg_Gimenez_et_al'), ('Nitrogen_Glarborg_Lucassen_et_al', 'Nitrogen_Glarborg_Lucassen_et_al'), ('Nitrogen_Glarborg_Zhang_et_al', 'Nitrogen_Glarborg_Zhang_et_al'), ('Sulfur/DMDS', 'Sulfur/DMDS'), ('Sulfur/DMS', 'Sulfur/DMS'), ('Sulfur/DTBS', 'Sulfur/DTBS'), ('Sulfur/GlarborgBozzelli', 'Sulfur/GlarborgBozzelli'), ('Sulfur/GlarborgH2S', 'Sulfur/GlarborgH2S'), ('Sulfur/GlarborgH2S/alt', 'Sulfur/GlarborgH2S/alt'), ('Sulfur/GlarborgMarshall', 'Sulfur/GlarborgMarshall'), ('Sulfur/GlarborgNS', 'Sulfur/GlarborgNS'), ('Sulfur/HSSH_1bar', 'Sulfur/HSSH_1bar'), ('Sulfur/Hexanethial_nr', 'Sulfur/Hexanethial_nr'), ('Sulfur/Sendt', 'Sulfur/Sendt'), ('Sulfur/TP_Song', 'Sulfur/TP_Song'), ('Sulfur/Thial_Hydrolysis', 'Sulfur/Thial_Hydrolysis'), ('Surface/CPOX_Pt/Deutschmann2006', 'Surface/CPOX_Pt/Deutschmann2006'), ('Surface/Deutschmann_Ni', 'Surface/Deutschmann_Ni'), ('Surface/Deutschmann_Ni_full', 'Surface/Deutschmann_Ni_full'), ('Surface/Example', 'Surface/Example'), ('TEOS', 'TEOS'), ('biCPD_H_shift', 'biCPD_H_shift'), ('c-C5H5_CH3_Sharma', 'c-C5H5_CH3_Sharma'), ('combustion_core/version2', 'combustion_core/version2'), ('combustion_core/version3', 'combustion_core/version3'), ('combustion_core/version4', 'combustion_core/version4'), ('combustion_core/version5', 'combustion_core/version5'), ('fascella', 'fascella'), ('kislovB', 'kislovB'), ('naphthalene_H', 'naphthalene_H'), ('primaryNitrogenLibrary', 'primaryNitrogenLibrary'), ('primaryNitrogenLibrary/LowT', 'primaryNitrogenLibrary/LowT'), ('primarySulfurLibrary', 'primarySulfurLibrary'), ('testSeed', 'testSeed'), ('testSeed_edge', 'testSeed_edge'), ('vinylCPD_H', 'vinylCPD_H')], max_length=200),
        ),
        migrations.AlterField(
            model_name='thermolibrary',
            name='thermo_lib',
            field=models.CharField(blank=True, choices=[('BurcatNS', 'BurcatNS'), ('BurkeH2O2', 'BurkeH2O2'), ('C10H11', 'C10H11'), ('C3', 'C3'), ('CBS_QB3_1dHR', 'CBS_QB3_1dHR'), ('CH', 'CH'), ('CHN', 'CHN'), ('CHO', 'CHO'), ('CHON', 'CHON'), ('CN', 'CN'), ('Chernov', 'Chernov'), ('Chlorinated_Hydrocarbons', 'Chlorinated_Hydrocarbons'), ('CurranPentane', 'CurranPentane'), ('DFT_QCI_thermo', 'DFT_QCI_thermo'), ('FFCM1(-)', 'FFCM1(-)'), ('Fulvene_H', 'Fulvene_H'), ('GRI-Mech3.0', 'GRI-Mech3.0'), ('GRI-Mech3.0-N', 'GRI-Mech3.0-N'), ('JetSurF1.0', 'JetSurF1.0'), ('JetSurF2.0', 'JetSurF2.0'), ('Klippenstein_Glarborg2016', 'Klippenstein_Glarborg2016'), ('Lai_Hexylbenzene', 'Lai_Hexylbenzene'), ('NISTThermoLibrary', 'NISTThermoLibrary'), ('NOx2018', 'NOx2018'), ('Narayanaswamy', 'Narayanaswamy'), ('NitrogenCurran', 'NitrogenCurran'), ('SABIC_aromatics', 'SABIC_aromatics'), ('SulfurGlarborgBozzelli', 'SulfurGlarborgBozzelli'), ('SulfurGlarborgH2S', 'SulfurGlarborgH2S'), ('SulfurGlarborgMarshall', 'SulfurGlarborgMarshall'), ('SulfurGlarborgNS', 'SulfurGlarborgNS'), ('SulfurHaynes', 'SulfurHaynes'), ('SulfurLibrary', 'SulfurLibrary'), ('USC-Mech-ii', 'USC-Mech-ii'), ('bio_oil', 'bio_oil'), ('iodinated_Hydrocarbons', 'iodinated_Hydrocarbons'), ('naphthalene_H', 'naphthalene_H'), ('primaryNS', 'primaryNS'), ('primaryThermoLibrary', 'primaryThermoLibrary'), ('surfaceThermoNi', 'surfaceThermoNi'), ('surfaceThermoPt', 'surfaceThermoPt'), ('thermo_DFT_CCSDTF12_BAC', 'thermo_DFT_CCSDTF12_BAC'), ('vinylCPD_H', 'vinylCPD_H')], max_length=200),
        ),
    ]
