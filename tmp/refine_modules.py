import os
import re

files_to_check = [
    'src/modules/strategy/StrategyModule.tsx',
    'src/modules/commercial/CommercialModule.tsx',
    'src/modules/finance/FinanceModule.tsx',
    'src/modules/units/UnitsModule.tsx',
    'src/modules/team/TeamModule.tsx',
    'src/modules/assets/AssetsModule.tsx',
    'src/modules/partners/PartnersModule.tsx',
    'src/modules/knowledge/KnowledgeModule.tsx',
    'src/modules/documents/DocumentsModule.tsx',
    'src/modules/occurrences/OccurrencesModule.tsx',
    'src/modules/audit/AuditModule.tsx',
    'src/modules/settings/SettingsModule.tsx',
    'src/modules/mywork/MyWorkModule.tsx',
    'src/modules/reports/ReportsModule.tsx',
    'src/components/modals/RealizationModal.tsx',
    'src/components/modals/ReservationWizardModal.tsx',
    'src/components/drawers/ReservationDetailDrawer.tsx',
    'src/components/drawers/VolumeDetailDrawer.tsx',
    'src/components/drawers/Customer360Drawer.tsx',
]

def transform_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Spacing
    content = content.replace('space-y-6 pb-12', 'space-y-4 pb-10')
    content = content.replace('space-y-6 pb-10', 'space-y-4 pb-10')

    # 2. Rounded classes
    content = re.sub(r'\brounded-3xl\b', 'rounded', content)
    content = re.sub(r'\brounded-2xl\b', 'rounded', content)
    content = re.sub(r'\brounded-xl\b', 'rounded', content)
    content = re.sub(r'\brounded-lg\b', 'rounded', content)

    # 3. Old tab active/inactive styling
    content = re.sub(r"'bg-amber-500 text-slate-950 font-bold'", "'bg-white text-slate-900 font-semibold shadow-xs'", content)
    content = re.sub(r"'bg-amber-500 text-slate-950 font-extrabold'", "'bg-white text-slate-900 font-semibold shadow-xs'", content)
    content = re.sub(r"'bg-amber-500 text-slate-950'", "'bg-white text-slate-900 font-semibold shadow-xs'", content)
    content = re.sub(r"'text-slate-500 hover:text-slate-800'", "'text-slate-600 hover:text-slate-900'", content)
    content = re.sub(r"'text-slate-500 hover:text-slate-700'", "'text-slate-600 hover:text-slate-900'", content)

    # 4. Old tab container
    content = re.sub(r'bg-slate-50/90 border border-slate-200 rounded', 'bg-slate-100 p-0.5 rounded text-xs', content)
    content = re.sub(r'p-1 bg-slate-50 border border-slate-200 rounded', 'p-0.5 bg-slate-100 rounded text-xs', content)
    content = re.sub(r'p-1 bg-slate-100 rounded', 'p-0.5 bg-slate-100 rounded text-xs', content)

    # 5. Buttons
    content = content.replace('bg-amber-500 hover:bg-amber-400 text-slate-950', 'bg-amber-600 hover:bg-amber-700 text-white')
    content = content.replace('bg-amber-500 text-slate-950', 'bg-amber-600 hover:bg-amber-700 text-white font-medium')
    content = content.replace('shadow-sm shadow-amber-500/20', '')
    content = content.replace('shadow-amber-500/20', '')
    content = content.replace('shadow-amber-500/30', '')
    content = content.replace('shadow-2xl', 'shadow-lg')

    # 6. Headers
    content = content.replace('font-extrabold', 'font-bold')
    content = content.replace('text-xl font-bold text-slate-900 tracking-tight mt-0.5', 'text-sm font-bold text-slate-900 tracking-tight')

    # 7. Card headers and structures
    content = content.replace('bg-white/90 p-5 rounded border border-slate-200', 'bg-white border border-slate-200 rounded p-3.5')
    content = content.replace('bg-white/90 p-4 rounded border border-slate-200', 'bg-white border border-slate-200 rounded p-3')

    # 8. Table header styling
    content = content.replace('border-b border-slate-200 text-[10px] font-mono text-slate-500 uppercase', 'bg-slate-50 border-b border-slate-200 text-[11px] text-slate-600 font-semibold')
    content = content.replace('border-b border-slate-200 text-[11px] font-mono text-slate-500 uppercase', 'bg-slate-50 border-b border-slate-200 text-[11px] text-slate-600 font-semibold')

    # 9. Clean up any accidental double spaces
    content = re.sub(r' +', ' ', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes: {filepath}")

for fp in files_to_check:
    transform_file(fp)
