html_content = """<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>KINETIC | Advisory & Consulting</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700;900&family=Manrope:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#ff915a",
                        "surface-container-low": "#131313",
                        "surface-container-high": "#201f1f",
                        "surface-container-lowest": "#090909",
                        "on-surface-variant": "#adaaaa",
                    },
                    fontFamily: {
                        "headline": ["Space Grotesk"],
                        "body": ["Manrope"],
                        "mono": ["ui-monospace", "SFMono-Regular", "monospace"]
                    }
                }
            }
        }
    </script>
    <style>
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24; }
        .glass-panel {
            background: rgba(20, 20, 20, 0.4);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .structured-grid {
            background-image: 
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px), 
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 50px 50px;
        }
        .btn-primary { box-shadow: 0 4px 14px rgba(255, 106, 0, 0.15); }
        .btn-primary:hover {
            box-shadow: 0 6px 20px rgba(255, 145, 90, 0.25);
            transform: translateY(-1px);
        }
        .card-struct {
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, transparent 100%);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .card-struct:hover {
            border-color: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
            background: rgba(30,30,30,0.5);
        }
        .connector-glow {
            background: linear-gradient(90deg, rgba(255,145,90,0.4) 0%, rgba(255,145,90,0.05) 100%);
        }
        .section-gradient {
            background: linear-gradient(180deg, rgba(11,11,11,0) 0%, rgba(15,15,15,1) 50%, rgba(11,11,11,0) 100%);
        }
    </style>
</head>
<body class="bg-[#0b0b0b] text-white font-body selection:bg-primary selection:text-black antialiased">

<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 h-20 bg-[#0b0b0b]/90 backdrop-blur-xl border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex justify-between items-center">
        <div class="text-2xl font-black tracking-tighter text-white font-headline">KINETIC</div>
        <div class="hidden md:flex items-center space-x-12">
            <a class="font-headline uppercase tracking-tighter text-[11px] font-bold transition-colors duration-300 text-white/50 hover:text-primary" href="home.html">ABOUT</a>
            <a class="font-headline uppercase tracking-tighter text-[11px] font-bold transition-colors duration-300 text-primary" href="advisory.html">ADVISORY</a>
            <a class="font-headline uppercase tracking-tighter text-[11px] font-bold transition-colors duration-300 text-white/50 hover:text-primary" href="#">ACADEMY</a>
            <a class="font-headline uppercase tracking-tighter text-[11px] font-bold transition-colors duration-300 text-white/50 hover:text-primary" href="#">CONTACT</a>
        </div>
        <button class="bg-surface-container-high hover:bg-[#ff7a31] border border-white/10 hover:border-[#ff7a31] transition-all duration-300 font-headline uppercase tracking-tighter text-[11px] font-bold px-7 py-2.5 rounded text-white hidden md:block">
            Client Portal
        </button>
    </div>
</nav>

<main class="pt-0">
    <!-- 1. HERO SECTION -->
    <section class="relative min-h-[90vh] flex flex-col justify-center overflow-hidden cyber-grid structured-grid border-b border-white/5">
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#111] via-[#0b0b0b] to-[#0b0b0b] z-0"></div>
        <div class="absolute top-[10%] right-[10%] w-[500px] h-[500px] bg-primary/5 blur-[100px] rounded-full mix-blend-screen pointer-events-none"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center py-24 md:py-32 mt-10">
            <div class="lg:col-span-7 flex flex-col justify-center relative">
                <div class="flex items-center gap-3 mb-6">
                    <div class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-50"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-primary"></span>
                    </div>
                    <span class="text-[10px] font-mono tracking-[0.2em] text-primary/80 uppercase">Consulting Practice . ACTIVE</span>
                </div>
                
                <h1 class="text-4xl sm:text-5xl lg:text-[4.5rem] font-headline font-black leading-[1.1] sm:leading-[1.05] tracking-tighter mb-8">
                    Strategic Risk Advisory <br>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-[#ffaa77]">For Enterprise Readiness</span>
                </h1>
                
                <p class="text-on-surface-variant text-lg font-light mb-10 leading-relaxed max-w-[540px] border-l border-white/10 pl-5">
                    We align digital risk protocols, cybersecurity frameworks, and emerging AI governance for continuous sovereign protection.
                </p>
                
                <div class="flex flex-wrap items-center gap-5">
                    <button class="px-8 py-3.5 bg-primary text-white font-headline font-semibold uppercase tracking-wider text-xs rounded transition-all btn-primary hover:-translate-y-0.5">
                        Schedule Consultation
                    </button>
                    <button class="px-8 py-3.5 border border-white/10 bg-white/[0.02] text-white font-headline font-semibold uppercase tracking-wider text-xs rounded transition-all hover:bg-white/[0.05] hover:-translate-y-0.5">
                        View Capabilities
                    </button>
                </div>
            </div>

            <!-- Controlled System Node Visual -->
            <div class="lg:col-span-5 relative w-full h-full min-h-[450px] flex justify-end items-center hidden lg:flex">
                <div class="relative w-full max-w-[450px] aspect-square rounded-2xl p-2 bg-gradient-to-br from-white/[0.03] to-transparent border border-white/5 shadow-2xl backdrop-blur-md">
                    <div class="relative w-full h-full bg-[#0d0d0d] rounded-xl border border-white/5 overflow-hidden flex flex-col justify-center items-center">
                        
                        <div class="absolute top-5 left-5 font-mono text-[9px] text-white/40 tracking-widest uppercase">Framework 0.4.1</div>
                        <div class="absolute bottom-5 right-5 font-mono text-[9px] text-white/40 tracking-widest uppercase flex items-center gap-2">
                            Sync <div class="w-8 h-[1px] bg-white/20"></div> 100%
                        </div>

                        <!-- Simplified System Graphic -->
                        <div class="relative w-56 h-56">
                            <!-- Single Clean Ring -->
                            <div class="absolute inset-0 rounded-full border border-primary/20 animate-[spin_20s_linear_infinite]"></div>
                            
                            <div class="absolute inset-10 rounded-full border border-white/5 bg-[#111] z-10 flex items-center justify-center shadow-inner">
                                <span class="material-symbols-outlined text-primary/80 text-4xl">account_tree</span>
                            </div>
                            
                            <!-- Floating Elements (Subtle) -->
                            <div class="absolute top-2 left-6 w-8 h-8 rounded-full border border-white/10 bg-[#0b0b0b] flex items-center justify-center z-20">
                                <span class="w-1.5 h-1.5 rounded-full bg-primary/60"></span>
                            </div>
                            <div class="absolute bottom-2 right-6 w-8 h-8 rounded border border-white/10 bg-[#0b0b0b] flex items-center justify-center z-20">
                                <span class="material-symbols-outlined text-white/50 text-xs">security</span>
                            </div>
                            <!-- Crosshairs -->
                            <div class="absolute top-1/2 -left-8 w-6 h-[1px] bg-white/10"></div>
                            <div class="absolute top-1/2 -right-8 w-6 h-[1px] bg-white/10"></div>
                            <div class="absolute -top-8 left-1/2 w-[1px] h-6 bg-white/10"></div>
                            <div class="absolute -bottom-8 left-1/2 w-[1px] h-6 bg-white/10"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. PROBLEMS WE SOLVE -->
    <section class="py-20 md:py-28 relative section-gradient">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="mb-12 md:mb-16 flex flex-col items-center text-center">
                <span class="font-mono text-[10px] uppercase tracking-widest text-primary/70 mb-3">Vulnerability Matrix</span>
                <h2 class="text-3xl md:text-4xl font-headline font-bold">The Risks We Navigate</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Cards -->
                <div class="glass-panel p-8 rounded-xl card-struct flex flex-col group transition-all duration-300">
                    <div class="w-14 h-14 rounded bg-[#0b0b0b] border border-white/5 flex items-center justify-center mb-6 group-hover:border-primary/30 transition-colors">
                        <span class="material-symbols-outlined text-white/70 text-3xl group-hover:text-primary transition-colors">lan</span>
                    </div>
                    <h3 class="font-headline font-bold text-lg mb-2 text-white">Fragmented Security</h3>
                    <p class="text-sm text-on-surface-variant font-light leading-relaxed">Disjointed tools creating critical visibility gaps across the attack surface.</p>
                </div>
                
                <div class="glass-panel p-8 rounded-xl card-struct flex flex-col group transition-all duration-300">
                    <div class="w-14 h-14 rounded bg-[#0b0b0b] border border-white/5 flex items-center justify-center mb-6 group-hover:border-primary/30 transition-colors">
                        <span class="material-symbols-outlined text-white/70 text-3xl group-hover:text-primary transition-colors">gavel</span>
                    </div>
                    <h3 class="font-headline font-bold text-lg mb-2 text-white">Regulatory Pressure</h3>
                    <p class="text-sm text-on-surface-variant font-light leading-relaxed">Increasing global mandates and penalties for complex data non-compliance.</p>
                </div>
                
                <div class="glass-panel p-8 rounded-xl card-struct flex flex-col group transition-all duration-300">
                    <div class="w-14 h-14 rounded bg-[#0b0b0b] border border-white/5 flex items-center justify-center mb-6 group-hover:border-primary/30 transition-colors">
                        <span class="material-symbols-outlined text-white/70 text-3xl group-hover:text-primary transition-colors">smart_toy</span>
                    </div>
                    <h3 class="font-headline font-bold text-lg mb-2 text-white">AI & Emerging Risk</h3>
                    <p class="text-sm text-on-surface-variant font-light leading-relaxed">Unregulated AI adoption introducing novel vulnerabilities and leakage paths.</p>
                </div>

                <div class="glass-panel p-8 rounded-xl card-struct flex flex-col group transition-all duration-300">
                    <div class="w-14 h-14 rounded bg-[#0b0b0b] border border-white/5 flex items-center justify-center mb-6 group-hover:border-primary/30 transition-colors">
                        <span class="material-symbols-outlined text-white/70 text-3xl group-hover:text-primary transition-colors">warning</span>
                    </div>
                    <h3 class="font-headline font-bold text-lg mb-2 text-white">Operational Drag</h3>
                    <p class="text-sm text-on-surface-variant font-light leading-relaxed">Legacy infrastructure impairing rapid response capabilities during incidents.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. CORE ADVISORY CAPABILITIES -->
    <section class="py-20 md:py-28 relative overflow-hidden bg-[#0a0a0a]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="mb-14 flex flex-col justify-center">
                <div class="w-8 h-[2px] bg-primary/60 mb-4"></div>
                <span class="font-mono text-[10px] uppercase tracking-widest text-primary/70 mb-2">Core Expertise</span>
                <h2 class="text-3xl md:text-4xl font-headline font-bold">Advisory Capabilities</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- capability 1 -->
                <div class="p-10 lg:p-12 glass-panel border border-white/10 hover:border-primary/30 rounded-xl group transition-all flex flex-col justify-between bg-gradient-to-br from-white/[0.04] to-transparent">
                    <div>
                        <span class="material-symbols-outlined text-primary/80 text-4xl mb-6 block">policy</span>
                        <h3 class="text-2xl font-headline font-bold mb-4">Digital Risk Audits</h3>
                        <p class="text-on-surface-variant mb-10 font-light leading-relaxed">Comprehensive mapping of your technological architecture to identify structural weaknesses before they are exploited. Assesses network perimeters, cloud environments, and internal access controls.</p>
                    </div>
                    
                    <div class="border-t border-white/5 pt-6 mt-auto">
                        <div class="flex items-center gap-3">
                            <div class="w-1.5 h-1.5 rounded-full bg-primary"></div>
                            <p class="text-sm text-white/90 font-medium">Identify vulnerabilities across enterprise vectors.</p>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col gap-8 flex-grow">
                    <!-- capability 2 -->
                    <div class="p-8 glass-panel border border-white/10 hover:border-primary/20 bg-gradient-to-br from-white/[0.04] to-transparent rounded-xl group transition-all flex flex-col justify-between flex-1">
                        <div>
                            <div class="flex justify-between items-start mb-3">
                                <h3 class="text-xl font-headline font-bold">Cyber Resilience Strategy</h3>
                                <span class="material-symbols-outlined text-white/30 text-2xl group-hover:text-primary transition-colors">deployed_code</span>
                            </div>
                            <p class="text-sm text-on-surface-variant mb-6 font-light leading-relaxed">Shifting from reactive defense to proactive continuity. We design intelligent incident response playbooks and disaster recovery architecture.</p>
                        </div>
                        <div class="flex items-center gap-3 border-t border-white/5 pt-4 mt-auto">
                            <p class="text-xs text-white/60 font-medium uppercase tracking-wide">Minimize downtime & rapid recovery</p>
                        </div>
                    </div>

                    <!-- capability 3 -->
                    <div class="p-8 glass-panel border border-white/10 hover:border-primary/20 bg-gradient-to-br from-white/[0.04] to-transparent rounded-xl group transition-all flex flex-col justify-between flex-1">
                        <div>
                            <div class="flex justify-between items-start mb-3">
                                <h3 class="text-xl font-headline font-bold">AI Risk Governance</h3>
                                <span class="material-symbols-outlined text-white/30 text-2xl group-hover:text-primary transition-colors">psychology</span>
                            </div>
                            <p class="text-sm text-on-surface-variant mb-6 font-light leading-relaxed">Establishing guardrails for enterprise AI adoption. Safe usage policies, model evaluation criteria, and strict corporate data security.</p>
                        </div>
                        <div class="flex items-center gap-3 border-t border-white/5 pt-4 mt-auto">
                            <p class="text-xs text-white/60 font-medium uppercase tracking-wide">Accelerate innovation safely</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. PROCESS / METHODOLOGY (Refined Flow) -->
    <section class="py-20 md:py-28 relative bg-[#0b0b0b] border-y border-white/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-20">
                <span class="font-mono text-[10px] uppercase tracking-widest text-primary/70 mb-3 block">Systematic Execution</span>
                <h2 class="text-3xl md:text-4xl font-headline font-bold">Strategic Methodology</h2>
            </div>

            <div class="relative max-w-5xl mx-auto">
                <!-- Flow Line -->
                <div class="hidden md:block absolute top-[20px] left-[10%] right-[10%] h-[2px] bg-white/5 z-0"></div>
                <div class="hidden md:block absolute top-[20px] left-[10%] right-[50%] h-[2px] bg-gradient-to-r from-primary/80 via-primary/40 to-transparent z-0 shadow-[0_0_10px_rgba(255,145,90,0.3)]"></div>
                
                <div class="grid grid-cols-1 md:grid-cols-5 gap-8 relative z-10">
                    <!-- Step 1 (Active) -->
                    <div class="flex flex-col items-center text-center">
                        <div class="w-10 h-10 bg-primary/10 border border-primary text-primary rounded-full flex items-center justify-center font-mono text-xs font-bold mb-5 shadow-[0_0_15px_rgba(255,106,0,0.2)] z-10 ring-4 ring-[#0b0b0b]">01</div>
                        <h4 class="font-headline font-semibold text-base mb-1">Assess</h4>
                        <p class="text-xs text-on-surface-variant font-light px-2">Complete architecture audit.</p>
                    </div>
                    <!-- Step 2 -->
                    <div class="flex flex-col items-center text-center">
                        <div class="w-10 h-10 bg-[#090909] border border-white/20 text-white/80 rounded-full flex items-center justify-center font-mono text-xs font-bold mb-5 z-10 ring-4 ring-[#0b0b0b]">02</div>
                        <h4 class="font-headline font-semibold text-base mb-1">Analyze</h4>
                        <p class="text-xs text-on-surface-variant font-light px-2">Threat and gap identification.</p>
                    </div>
                    <!-- Step 3 -->
                    <div class="flex flex-col items-center text-center">
                        <div class="w-10 h-10 bg-[#090909] border border-white/20 text-white/80 rounded-full flex items-center justify-center font-mono text-xs font-bold mb-5 z-10 ring-4 ring-[#0b0b0b]">03</div>
                        <h4 class="font-headline font-semibold text-base mb-1">Design</h4>
                        <p class="text-xs text-on-surface-variant font-light px-2">Secure structural frameworks.</p>
                    </div>
                    <!-- Step 4 -->
                    <div class="flex flex-col items-center text-center">
                        <div class="w-10 h-10 bg-[#090909] border border-white/20 text-white/80 rounded-full flex items-center justify-center font-mono text-xs font-bold mb-5 z-10 ring-4 ring-[#0b0b0b]">04</div>
                        <h4 class="font-headline font-semibold text-base mb-1">Implement</h4>
                        <p class="text-xs text-on-surface-variant font-light px-2">Strict operational controls.</p>
                    </div>
                    <!-- Step 5 -->
                    <div class="flex flex-col items-center text-center">
                        <div class="w-10 h-10 bg-[#090909] border border-white/20 text-white/80 rounded-full flex items-center justify-center font-mono text-xs font-bold mb-5 z-10 ring-4 ring-[#0b0b0b]">05</div>
                        <h4 class="font-headline font-semibold text-base mb-1">Optimize</h4>
                        <p class="text-xs text-on-surface-variant font-light px-2">Continuous environment scaling.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. FRAMEWORK & 6. OUTCOMES -->
    <section class="py-20 md:py-28 relative overflow-hidden">
        <div class="absolute top-1/2 left-0 w-[400px] h-[400px] bg-primary/5 blur-[120px] pointer-events-none mix-blend-screen overflow-hidden"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
                
                <!-- Framework Alignment -->
                <div class="flex flex-col justify-center">
                    <h2 class="text-3xl font-headline font-bold mb-4">Global Standards</h2>
                    <p class="text-on-surface-variant font-light mb-12 text-sm leading-relaxed max-w-lg">Our methodologies align closely with rigorous international cybersecurity regulations, ensuring audit readiness everywhere.</p>
                    
                    <div class="grid grid-cols-2 gap-x-8 gap-y-12">
                        <div class="flex items-start gap-4 group">
                            <span class="material-symbols-outlined text-white/30 text-4xl group-hover:text-primary transition-colors">account_balance</span>
                            <div>
                                <div class="font-headline font-semibold text-white">NIST</div>
                                <div class="text-[10px] text-white/50 uppercase tracking-widest mt-1">Risk Framework</div>
                            </div>
                        </div>
                        <div class="flex items-start gap-4 group">
                            <span class="material-symbols-outlined text-white/30 text-4xl group-hover:text-primary transition-colors">verified_user</span>
                            <div>
                                <div class="font-headline font-semibold text-white">ISO 27001</div>
                                <div class="text-[10px] text-white/50 uppercase tracking-widest mt-1">Security Standard</div>
                            </div>
                        </div>
                        <div class="flex items-start gap-4 group">
                            <span class="material-symbols-outlined text-white/30 text-4xl group-hover:text-primary transition-colors">public</span>
                            <div>
                                <div class="font-headline font-semibold text-white">GDPR</div>
                                <div class="text-[10px] text-white/50 uppercase tracking-widest mt-1">Data Compliance</div>
                            </div>
                        </div>
                        <div class="flex items-start gap-4 group">
                            <span class="material-symbols-outlined text-white/30 text-4xl group-hover:text-primary transition-colors">psychology</span>
                            <div>
                                <div class="font-headline font-semibold text-white">AI Governance</div>
                                <div class="text-[10px] text-white/50 uppercase tracking-widest mt-1">Ethics & Risk</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Outcomes List -->
                <div class="glass-panel p-10 lg:p-12 rounded-2xl border border-white/5">
                    <h2 class="text-2xl font-headline font-bold mb-3">What You Gain</h2>
                    <p class="text-on-surface-variant font-light mb-8 text-sm pb-8 border-b border-white/5">Mitigate downside and confidently enable secure enterprise expansion.</p>
                    
                    <div class="flex flex-col gap-8">
                        <div class="flex gap-5 items-start">
                            <span class="material-symbols-outlined text-primary text-2xl mt-0.5">task_alt</span>
                            <div>
                                <h4 class="font-headline text-lg font-semibold text-white mb-1">Reduced Risk Exposure</h4>
                                <p class="text-sm text-on-surface-variant font-light">Measurable, continuous decrease in external attack surface vectors.</p>
                            </div>
                        </div>
                        <div class="flex gap-5 items-start">
                            <span class="material-symbols-outlined text-primary text-2xl mt-0.5">task_alt</span>
                            <div>
                                <h4 class="font-headline text-lg font-semibold text-white mb-1">Regulatory Readiness</h4>
                                <p class="text-sm text-on-surface-variant font-light">Audit-ready documentation and structural policy framework delivery.</p>
                            </div>
                        </div>
                        <div class="flex gap-5 items-start">
                            <span class="material-symbols-outlined text-white/50 text-2xl mt-0.5">layers</span>
                            <div>
                                <h4 class="font-headline text-lg font-semibold text-white mb-1">Scalable Infrastructure</h4>
                                <p class="text-sm text-on-surface-variant font-light">Security foundations dynamically architected to grow with operations.</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 7. CASE STUDY / PROOF (Refined Typography) -->
    <section class="py-20 md:py-28 relative bg-[#090909] border-y border-white/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="flex flex-col lg:flex-row justify-between gap-16 items-center">
                <div class="lg:w-1/2">
                    <div class="flex items-center gap-3 mb-8">
                        <div class="w-4 h-[1px] bg-primary/60"></div>
                        <div class="font-mono text-[10px] text-white/50 tracking-widest uppercase">Case Platform Metric</div>
                    </div>
                    <h3 class="text-3xl lg:text-4xl font-headline font-bold mb-6">Global Platform Overhaul</h3>
                    <p class="text-base text-on-surface-variant font-light leading-relaxed mb-8 max-w-lg">Assessed and completely rebuilt legacy architecture for a Fortune 500 entity, implementing functional zero-trust network access and automated compliance routing.</p>
                    <button class="text-xs font-mono text-primary font-bold tracking-widest uppercase hover:underline flex items-center gap-2 group">
                        Review Case Data <span class="material-symbols-outlined text-sm group-hover:translate-x-1 transition-transform">arrow_forward</span>
                    </button>
                </div>
                
                <div class="lg:w-1/2 w-full grid grid-cols-2 gap-12 lg:pl-16 lg:border-l border-white/10">
                    <div class="flex flex-col">
                        <div class="text-[5rem] lg:text-[6rem] font-headline font-black text-white leading-none tracking-tighter mb-4">40<span class="text-primary text-5xl align-top block lg:inline mt-2 lg:mt-0 lg:ml-1">%</span></div>
                        <h4 class="font-headline font-bold text-lg mb-2 text-white">Vulnerability Drop</h4>
                        <div class="text-xs text-white/50 font-light leading-relaxed">System-wide attack surfaces neutralized successfully.</div>
                    </div>
                    <div class="flex flex-col">
                        <div class="text-[5rem] lg:text-[6rem] font-headline font-black text-white leading-none tracking-tighter mb-4">3<span class="text-primary text-5xl align-top block lg:inline mt-2 lg:mt-0 lg:ml-1">x</span></div>
                        <h4 class="font-headline font-bold text-lg mb-2 text-white">Audit Speed</h4>
                        <div class="text-xs text-white/50 font-light leading-relaxed">Acceleration of regular enterprise compliance checks.</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. FINAL CTA SECTION (Controlled Impact) -->
    <section class="py-20 md:py-28 relative overflow-hidden">
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[350px] h-[350px] bg-primary/10 blur-[150px] pointer-events-none rounded-full"></div>

        <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10 flex flex-col items-center">
            <div class="w-14 h-14 border border-white/10 rounded flex items-center justify-center bg-[#090909] mb-8 shadow-lg">
                <span class="material-symbols-outlined text-white/80 text-2xl">shield_lock</span>
            </div>
            <h2 class="text-4xl md:text-5xl font-headline font-bold mb-6 tracking-tight">Secure Your Infrastructure</h2>
            <p class="text-lg text-on-surface-variant font-light mb-8 leading-relaxed max-w-xl">Partner with Kinetic to establish uncompromised enterprise readiness from the structural layer upward.</p>
            <div class="flex justify-center flex-wrap gap-4">
                <button class="px-12 py-4 bg-primary text-white font-headline font-semibold uppercase tracking-wider text-sm rounded shadow-[0_4px_15px_rgba(255,106,0,0.2)] transition-all hover:bg-[#ff7a31] hover:-translate-y-0.5">
                    Initiate Audit
                </button>
            </div>
        </div>
    </section>

</main>

<footer class="w-full py-16 px-4 sm:px-6 lg:px-8 bg-[#090909] text-sm relative">
    <div class="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-white/10 to-transparent"></div>
    <div class="grid grid-cols-1 md:grid-cols-4 gap-12 max-w-7xl mx-auto text-left relative z-10">
        <div class="md:col-span-1">
            <div class="text-xl font-black text-white font-headline mb-6 tracking-tighter">KINETIC</div>
            <p class="text-white/50 font-light mb-8 leading-relaxed text-xs max-w-[200px]">Strategic digital risk advisory building resilient environments for elite global enterprises.</p>
            <div class="flex gap-5">
                <span class="material-symbols-outlined text-white/40 text-lg cursor-pointer hover:text-white transition-colors">language</span>
                <span class="material-symbols-outlined text-white/40 text-lg cursor-pointer hover:text-white transition-colors">shield</span>
            </div>
        </div>
        <div class="md:col-span-3 grid grid-cols-2 md:grid-cols-3 gap-10">
            <div>
                <h5 class="font-mono font-bold text-white/80 mb-6 uppercase tracking-widest text-[10px]">Navigation</h5>
                <ul class="space-y-4">
                    <li><a class="text-white/50 hover:text-white transition-colors text-xs font-medium" href="home.html">ABOUT</a></li>
                    <li><a class="text-primary hover:text-[#ffaa77] transition-colors text-xs font-medium" href="advisory.html">ADVISORY</a></li>
                    <li><a class="text-white/50 hover:text-white transition-colors text-xs font-medium" href="#">ACADEMY</a></li>
                </ul>
            </div>
            <div>
                <h5 class="font-mono font-bold text-white/80 mb-6 uppercase tracking-widest text-[10px]">Legal</h5>
                <ul class="space-y-4">
                    <li><a class="text-white/50 hover:text-white transition-colors text-xs font-medium" href="#">Privacy Policy</a></li>
                    <li><a class="text-white/50 hover:text-white transition-colors text-xs font-medium" href="#">Terms of Service</a></li>
                    <li><a class="text-white/50 hover:text-white transition-colors text-xs font-medium" href="#">Security Index</a></li>
                </ul>
            </div>
            <div class="col-span-2 md:col-span-1 border-t border-white/5 pt-8 md:pt-0 md:border-t-0">
                <h5 class="font-mono font-bold text-white/80 mb-6 uppercase tracking-widest text-[10px]">Platform Access</h5>
                <div class="flex flex-col gap-3">
                    <input class="bg-white/[0.03] border border-white/10 text-white font-mono text-[10px] px-4 py-3 focus:border-primary outline-none placeholder:text-white/40 rounded transition-colors" placeholder="ENTER CLEARANCE EMAIL" type="email"/>
                    <button class="bg-white/10 text-white font-mono font-bold uppercase tracking-widest text-[10px] py-3 rounded hover:bg-primary transition-colors hover:text-black">Request Entry</button>
                </div>
            </div>
        </div>
    </div>
    <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6 relative z-10">
        <p class="text-white/30 font-mono text-[10px] tracking-widest uppercase">© 2024 KINETIC STRATEGIC ADVISORY</p>
        <div class="flex gap-8">
            <span class="text-white/30 font-mono text-[9px] tracking-widest flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-primary/80"></div> STATUS: SECURE</span>
            <span class="text-white/30 font-mono text-[9px] tracking-widest">NODE: KIN-01</span>
        </div>
    </div>
</footer>

</body>
</html>
"""

with open('c:\\Users\\sy753\\OneDrive\\Pictures\\AIML\\project kinetic assingment\\advisory.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'c:\Users\sy753\OneDrive\Pictures\AIML\project kinetic assingment\advisory.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
