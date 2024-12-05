<html>
<head>
<title>ArvoresAVL.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #2aacb8;}
.s4 { color: #7a7e85;}
.s5 { color: #6aab73;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
ArvoresAVL.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">csv</span>

<span class="s0">class </span><span class="s1">Node</span><span class="s2">:</span>
    <span class="s0">def </span><span class="s1">__init__</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">):</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">key </span><span class="s2">= </span><span class="s1">key</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">value </span><span class="s2">= </span><span class="s1">value</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">height </span><span class="s2">= </span><span class="s3">1</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">left </span><span class="s2">= </span><span class="s0">None</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">right </span><span class="s2">= </span><span class="s0">None</span>

<span class="s0">class </span><span class="s1">AVLTree</span><span class="s2">:</span>
    <span class="s0">def </span><span class="s1">__init__</span><span class="s2">(</span><span class="s1">self</span><span class="s2">):</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">root </span><span class="s2">= </span><span class="s0">None</span>

    <span class="s0">def </span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">node</span><span class="s2">):</span>
        <span class="s0">if not </span><span class="s1">node</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s3">0</span>
        <span class="s0">return </span><span class="s1">node</span><span class="s2">.</span><span class="s1">height</span>

    <span class="s0">def </span><span class="s1">get_balance</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">node</span><span class="s2">):</span>
        <span class="s0">if not </span><span class="s1">node</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s3">0</span>
        <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">) - </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">)</span>

    <span class="s0">def </span><span class="s1">rotate_right</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">y</span><span class="s2">):</span>
        <span class="s1">x </span><span class="s2">= </span><span class="s1">y</span><span class="s2">.</span><span class="s1">left</span>
        <span class="s1">T </span><span class="s2">= </span><span class="s1">x</span><span class="s2">.</span><span class="s1">right</span>
        <span class="s1">x</span><span class="s2">.</span><span class="s1">right </span><span class="s2">= </span><span class="s1">y</span>
        <span class="s1">y</span><span class="s2">.</span><span class="s1">left </span><span class="s2">= </span><span class="s1">T</span>
        <span class="s1">y</span><span class="s2">.</span><span class="s1">height </span><span class="s2">= </span><span class="s3">1 </span><span class="s2">+ </span><span class="s1">max</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">y</span><span class="s2">.</span><span class="s1">left</span><span class="s2">), </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">y</span><span class="s2">.</span><span class="s1">right</span><span class="s2">))</span>
        <span class="s1">x</span><span class="s2">.</span><span class="s1">height </span><span class="s2">= </span><span class="s3">1 </span><span class="s2">+ </span><span class="s1">max</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">x</span><span class="s2">.</span><span class="s1">left</span><span class="s2">), </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">x</span><span class="s2">.</span><span class="s1">right</span><span class="s2">))</span>
        <span class="s0">return </span><span class="s1">x</span>

    <span class="s0">def </span><span class="s1">rotate_left</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">x</span><span class="s2">):</span>
        <span class="s1">y </span><span class="s2">= </span><span class="s1">x</span><span class="s2">.</span><span class="s1">right</span>
        <span class="s1">T </span><span class="s2">= </span><span class="s1">y</span><span class="s2">.</span><span class="s1">left</span>
        <span class="s1">y</span><span class="s2">.</span><span class="s1">left </span><span class="s2">= </span><span class="s1">x</span>
        <span class="s1">x</span><span class="s2">.</span><span class="s1">right </span><span class="s2">= </span><span class="s1">T</span>
        <span class="s1">x</span><span class="s2">.</span><span class="s1">height </span><span class="s2">= </span><span class="s3">1 </span><span class="s2">+ </span><span class="s1">max</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">x</span><span class="s2">.</span><span class="s1">left</span><span class="s2">), </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">x</span><span class="s2">.</span><span class="s1">right</span><span class="s2">))</span>
        <span class="s1">y</span><span class="s2">.</span><span class="s1">height </span><span class="s2">= </span><span class="s3">1 </span><span class="s2">+ </span><span class="s1">max</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">y</span><span class="s2">.</span><span class="s1">left</span><span class="s2">), </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">y</span><span class="s2">.</span><span class="s1">right</span><span class="s2">))</span>
        <span class="s0">return </span><span class="s1">y</span>

    <span class="s0">def </span><span class="s1">insert</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">node</span><span class="s2">, </span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">):</span>
        <span class="s0">if not </span><span class="s1">node</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s1">Node</span><span class="s2">(</span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">key </span><span class="s2">&lt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s1">node</span><span class="s2">.</span><span class="s1">left </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">insert</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">, </span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">)</span>
        <span class="s0">elif </span><span class="s1">key </span><span class="s2">&gt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s1">node</span><span class="s2">.</span><span class="s1">right </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">insert</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">, </span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">)</span>
        <span class="s0">else</span><span class="s2">:</span>
            <span class="s1">node</span><span class="s2">.</span><span class="s1">value </span><span class="s2">= </span><span class="s1">value  </span><span class="s4"># Update value if the key exists</span>
            <span class="s0">return </span><span class="s1">node</span>

        <span class="s1">node</span><span class="s2">.</span><span class="s1">height </span><span class="s2">= </span><span class="s3">1 </span><span class="s2">+ </span><span class="s1">max</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">), </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_height</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">))</span>
        <span class="s1">balance </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">get_balance</span><span class="s2">(</span><span class="s1">node</span><span class="s2">)</span>

        <span class="s4"># Balance cases</span>
        <span class="s0">if </span><span class="s1">balance </span><span class="s2">&gt; </span><span class="s3">1 </span><span class="s0">and </span><span class="s1">key </span><span class="s2">&lt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">rotate_right</span><span class="s2">(</span><span class="s1">node</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">balance </span><span class="s2">&lt; -</span><span class="s3">1 </span><span class="s0">and </span><span class="s1">key </span><span class="s2">&gt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">rotate_left</span><span class="s2">(</span><span class="s1">node</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">balance </span><span class="s2">&gt; </span><span class="s3">1 </span><span class="s0">and </span><span class="s1">key </span><span class="s2">&gt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s1">node</span><span class="s2">.</span><span class="s1">left </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">rotate_left</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">)</span>
            <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">rotate_right</span><span class="s2">(</span><span class="s1">node</span><span class="s2">)</span>
        <span class="s0">if </span><span class="s1">balance </span><span class="s2">&lt; -</span><span class="s3">1 </span><span class="s0">and </span><span class="s1">key </span><span class="s2">&lt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s1">node</span><span class="s2">.</span><span class="s1">right </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">rotate_right</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">)</span>
            <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">rotate_left</span><span class="s2">(</span><span class="s1">node</span><span class="s2">)</span>

        <span class="s0">return </span><span class="s1">node</span>

    <span class="s0">def </span><span class="s1">search</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">node</span><span class="s2">, </span><span class="s1">key</span><span class="s2">):</span>
        <span class="s0">if not </span><span class="s1">node </span><span class="s0">or </span><span class="s1">node</span><span class="s2">.</span><span class="s1">key </span><span class="s2">== </span><span class="s1">key</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s1">node</span>
        <span class="s0">if </span><span class="s1">key </span><span class="s2">&lt; </span><span class="s1">node</span><span class="s2">.</span><span class="s1">key</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">search</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">, </span><span class="s1">key</span><span class="s2">)</span>
        <span class="s0">return </span><span class="s1">self</span><span class="s2">.</span><span class="s1">search</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">, </span><span class="s1">key</span><span class="s2">)</span>

    <span class="s0">def </span><span class="s1">add</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">):</span>
        <span class="s1">self</span><span class="s2">.</span><span class="s1">root </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">insert</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">root</span><span class="s2">, </span><span class="s1">key</span><span class="s2">, </span><span class="s1">value</span><span class="s2">)</span>

    <span class="s0">def </span><span class="s1">find</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">key</span><span class="s2">):</span>
        <span class="s1">result </span><span class="s2">= </span><span class="s1">self</span><span class="s2">.</span><span class="s1">search</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">root</span><span class="s2">, </span><span class="s1">key</span><span class="s2">)</span>
        <span class="s0">return </span><span class="s1">result</span><span class="s2">.</span><span class="s1">value </span><span class="s0">if </span><span class="s1">result </span><span class="s0">else None</span>

    <span class="s0">def </span><span class="s1">calculate_averages</span><span class="s2">(</span><span class="s1">self</span><span class="s2">):</span>
        <span class="s4"># Percorrer a árvore e calcular a média de plaquetas, vitamina C e ferro</span>
        <span class="s1">plaquetas_sum </span><span class="s2">= </span><span class="s3">0</span>
        <span class="s1">vitamina_c_sum </span><span class="s2">= </span><span class="s3">0</span>
        <span class="s1">ferro_sum </span><span class="s2">= </span><span class="s3">0</span>
        <span class="s1">count </span><span class="s2">= </span><span class="s3">0</span>
        <span class="s1">patients </span><span class="s2">= []</span>

        <span class="s0">def </span><span class="s1">traverse</span><span class="s2">(</span><span class="s1">node</span><span class="s2">):</span>
            <span class="s0">nonlocal </span><span class="s1">plaquetas_sum</span><span class="s2">, </span><span class="s1">vitamina_c_sum</span><span class="s2">, </span><span class="s1">ferro_sum</span><span class="s2">, </span><span class="s1">count</span><span class="s2">, </span><span class="s1">patients</span>
            <span class="s0">if </span><span class="s1">node</span><span class="s2">:</span>
                <span class="s1">patients</span><span class="s2">.</span><span class="s1">append</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">value</span><span class="s2">)</span>
                <span class="s1">plaquetas_sum </span><span class="s2">+= </span><span class="s1">node</span><span class="s2">.</span><span class="s1">value</span><span class="s2">[</span><span class="s5">'plaquetas'</span><span class="s2">]</span>
                <span class="s1">vitamina_c_sum </span><span class="s2">+= </span><span class="s1">node</span><span class="s2">.</span><span class="s1">value</span><span class="s2">[</span><span class="s5">'vitamina_c'</span><span class="s2">]</span>
                <span class="s1">ferro_sum </span><span class="s2">+= </span><span class="s1">node</span><span class="s2">.</span><span class="s1">value</span><span class="s2">[</span><span class="s5">'ferro'</span><span class="s2">]</span>
                <span class="s1">count </span><span class="s2">+= </span><span class="s3">1</span>
                <span class="s1">traverse</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">left</span><span class="s2">)</span>
                <span class="s1">traverse</span><span class="s2">(</span><span class="s1">node</span><span class="s2">.</span><span class="s1">right</span><span class="s2">)</span>

        <span class="s1">traverse</span><span class="s2">(</span><span class="s1">self</span><span class="s2">.</span><span class="s1">root</span><span class="s2">)</span>

        <span class="s0">if </span><span class="s1">count </span><span class="s2">&gt; </span><span class="s3">0</span><span class="s2">:</span>
            <span class="s0">return </span><span class="s2">{</span>
                <span class="s5">&quot;average_plaquetas&quot;</span><span class="s2">: </span><span class="s1">plaquetas_sum </span><span class="s2">/ </span><span class="s1">count</span><span class="s2">,</span>
                <span class="s5">&quot;average_vitamina_c&quot;</span><span class="s2">: </span><span class="s1">vitamina_c_sum </span><span class="s2">/ </span><span class="s1">count</span><span class="s2">,</span>
                <span class="s5">&quot;average_ferro&quot;</span><span class="s2">: </span><span class="s1">ferro_sum </span><span class="s2">/ </span><span class="s1">count</span><span class="s2">,</span>
                <span class="s5">&quot;patients&quot;</span><span class="s2">: </span><span class="s1">patients</span>
            <span class="s2">}</span>
        <span class="s0">else</span><span class="s2">:</span>
            <span class="s0">return None</span>

    <span class="s0">def </span><span class="s1">check_health</span><span class="s2">(</span><span class="s1">self</span><span class="s2">, </span><span class="s1">patient</span><span class="s2">):</span>
        <span class="s4"># Definir os critérios de saúde</span>
        <span class="s1">healthy </span><span class="s2">= </span><span class="s0">True</span>
        <span class="s0">if </span><span class="s1">patient</span><span class="s2">[</span><span class="s5">'plaquetas'</span><span class="s2">] &lt; </span><span class="s3">150000 </span><span class="s0">or </span><span class="s1">patient</span><span class="s2">[</span><span class="s5">'plaquetas'</span><span class="s2">] &gt; </span><span class="s3">400000</span><span class="s2">:</span>
            <span class="s1">healthy </span><span class="s2">= </span><span class="s0">False</span>
        <span class="s0">if </span><span class="s1">patient</span><span class="s2">[</span><span class="s5">'vitamina_c'</span><span class="s2">] &lt; </span><span class="s3">0.6 </span><span class="s0">or </span><span class="s1">patient</span><span class="s2">[</span><span class="s5">'vitamina_c'</span><span class="s2">] &gt; </span><span class="s3">2.0</span><span class="s2">:</span>
            <span class="s1">healthy </span><span class="s2">= </span><span class="s0">False</span>
        <span class="s0">if </span><span class="s1">patient</span><span class="s2">[</span><span class="s5">'ferro'</span><span class="s2">] &lt; </span><span class="s3">60 </span><span class="s0">or </span><span class="s1">patient</span><span class="s2">[</span><span class="s5">'ferro'</span><span class="s2">] &gt; </span><span class="s3">160</span><span class="s2">:</span>
            <span class="s1">healthy </span><span class="s2">= </span><span class="s0">False</span>
        <span class="s0">return </span><span class="s1">healthy</span>


<span class="s4"># Carregar dados do CSV e construir a AVL Tree</span>
<span class="s0">def </span><span class="s1">carregar_dados_csv</span><span class="s2">(</span><span class="s1">arquivo_csv</span><span class="s2">):</span>
    <span class="s1">avl </span><span class="s2">= </span><span class="s1">AVLTree</span><span class="s2">()</span>
    <span class="s0">with </span><span class="s1">open</span><span class="s2">(</span><span class="s1">arquivo_csv</span><span class="s2">, </span><span class="s1">newline</span><span class="s2">=</span><span class="s5">''</span><span class="s2">, </span><span class="s1">encoding</span><span class="s2">=</span><span class="s5">'utf-8'</span><span class="s2">) </span><span class="s0">as </span><span class="s1">csvfile</span><span class="s2">:</span>
        <span class="s1">reader </span><span class="s2">= </span><span class="s1">csv</span><span class="s2">.</span><span class="s1">DictReader</span><span class="s2">(</span><span class="s1">csvfile</span><span class="s2">)</span>
        <span class="s0">for </span><span class="s1">row </span><span class="s0">in </span><span class="s1">reader</span><span class="s2">:</span>
            <span class="s1">key </span><span class="s2">= </span><span class="s1">int</span><span class="s2">(</span><span class="s1">row</span><span class="s2">[</span><span class="s5">'id'</span><span class="s2">])  </span><span class="s4"># Usando ID como chave</span>
            <span class="s1">row</span><span class="s2">[</span><span class="s5">'plaquetas'</span><span class="s2">] = </span><span class="s1">int</span><span class="s2">(</span><span class="s1">row</span><span class="s2">[</span><span class="s5">'plaquetas'</span><span class="s2">])  </span><span class="s4"># Converte plaquetas para inteiro</span>
            <span class="s1">row</span><span class="s2">[</span><span class="s5">'vitamina_c'</span><span class="s2">] = </span><span class="s1">float</span><span class="s2">(</span><span class="s1">row</span><span class="s2">[</span><span class="s5">'vitamina_c'</span><span class="s2">])  </span><span class="s4"># Converte vitamina C para float</span>
            <span class="s1">row</span><span class="s2">[</span><span class="s5">'ferro'</span><span class="s2">] = </span><span class="s1">float</span><span class="s2">(</span><span class="s1">row</span><span class="s2">[</span><span class="s5">'ferro'</span><span class="s2">])  </span><span class="s4"># Converte ferro para float</span>
            <span class="s1">avl</span><span class="s2">.</span><span class="s1">add</span><span class="s2">(</span><span class="s1">key</span><span class="s2">, </span><span class="s1">row</span><span class="s2">)</span>
    <span class="s0">return </span><span class="s1">avl</span>


<span class="s4"># Interface de busca</span>
<span class="s0">def </span><span class="s1">buscar_registro</span><span class="s2">(</span><span class="s1">avl</span><span class="s2">):</span>
    <span class="s0">while True</span><span class="s2">:</span>
        <span class="s0">try</span><span class="s2">:</span>
            <span class="s1">key </span><span class="s2">= </span><span class="s1">int</span><span class="s2">(</span><span class="s1">input</span><span class="s2">(</span><span class="s5">&quot;Digite o ID para buscar (ou -1 para sair): &quot;</span><span class="s2">))</span>
            <span class="s0">if </span><span class="s1">key </span><span class="s2">== -</span><span class="s3">1</span><span class="s2">:</span>
                <span class="s0">break</span>
            <span class="s1">resultado </span><span class="s2">= </span><span class="s1">avl</span><span class="s2">.</span><span class="s1">find</span><span class="s2">(</span><span class="s1">key</span><span class="s2">)</span>
            <span class="s0">if </span><span class="s1">resultado</span><span class="s2">:</span>
                <span class="s1">healthy_status </span><span class="s2">= </span><span class="s5">&quot;saudável&quot; </span><span class="s0">if </span><span class="s1">avl</span><span class="s2">.</span><span class="s1">check_health</span><span class="s2">(</span><span class="s1">resultado</span><span class="s2">) </span><span class="s0">else </span><span class="s5">&quot;não saudável&quot;</span>
                <span class="s1">print</span><span class="s2">(</span><span class="s5">f&quot;Registro encontrado: </span><span class="s0">{</span><span class="s1">resultado</span><span class="s0">}</span><span class="s5">&quot;</span><span class="s2">)</span>
                <span class="s1">print</span><span class="s2">(</span><span class="s5">f&quot;Status de saúde: </span><span class="s0">{</span><span class="s1">healthy_status</span><span class="s0">}</span><span class="s5">&quot;</span><span class="s2">)</span>
            <span class="s0">else</span><span class="s2">:</span>
                <span class="s1">print</span><span class="s2">(</span><span class="s5">&quot;Registro não encontrado.&quot;</span><span class="s2">)</span>
        <span class="s0">except </span><span class="s1">ValueError</span><span class="s2">:</span>
            <span class="s1">print</span><span class="s2">(</span><span class="s5">&quot;Por favor, insira um número válido.&quot;</span><span class="s2">)</span>


<span class="s4"># Função principal</span>
<span class="s0">if </span><span class="s1">__name__ </span><span class="s2">== </span><span class="s5">&quot;__main__&quot;</span><span class="s2">:</span>
    <span class="s1">arquivo_csv </span><span class="s2">= </span><span class="s5">&quot;dados_completos.csv&quot;  </span><span class="s4"># Nome do arquivo CSV</span>
    <span class="s1">avl_tree </span><span class="s2">= </span><span class="s1">carregar_dados_csv</span><span class="s2">(</span><span class="s1">arquivo_csv</span><span class="s2">)</span>
    <span class="s1">print</span><span class="s2">(</span><span class="s5">&quot;Dados carregados com sucesso.&quot;</span><span class="s2">)</span>

    <span class="s4"># Calcular médias de plaquetas, vitamina C e ferro</span>
    <span class="s1">averages </span><span class="s2">= </span><span class="s1">avl_tree</span><span class="s2">.</span><span class="s1">calculate_averages</span><span class="s2">()</span>
    <span class="s0">if </span><span class="s1">averages</span><span class="s2">:</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s5">f&quot;Média de plaquetas: </span><span class="s0">{</span><span class="s1">averages</span><span class="s2">[</span><span class="s5">'average_plaquetas'</span><span class="s2">]</span><span class="s0">}</span><span class="s5">&quot;</span><span class="s2">)</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s5">f&quot;Média de vitamina C: </span><span class="s0">{</span><span class="s1">averages</span><span class="s2">[</span><span class="s5">'average_vitamina_c'</span><span class="s2">]</span><span class="s0">}</span><span class="s5">&quot;</span><span class="s2">)</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s5">f&quot;Média de ferro: </span><span class="s0">{</span><span class="s1">averages</span><span class="s2">[</span><span class="s5">'average_ferro'</span><span class="s2">]</span><span class="s0">}</span><span class="s5">&quot;</span><span class="s2">)</span>
    <span class="s0">else</span><span class="s2">:</span>
        <span class="s1">print</span><span class="s2">(</span><span class="s5">&quot;Não há dados para calcular as médias.&quot;</span><span class="s2">)</span>

    <span class="s4"># Buscar registros</span>
    <span class="s1">buscar_registro</span><span class="s2">(</span><span class="s1">avl_tree</span><span class="s2">)</span>
</pre>
</body>
</html>