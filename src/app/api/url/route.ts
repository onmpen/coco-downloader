import { NextRequest, NextResponse } from 'next/server';
import { getProvider } from '@/lib/providers';

function parseExtra(value: string | null) {
  if (!value) return undefined;
  try {
    return JSON.parse(value) as unknown;
  } catch {
    return undefined;
  }
}

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const id = searchParams.get('id');
  const providerName = searchParams.get('provider') || 'netease';
  const extra = parseExtra(searchParams.get('extra'));

  if (!id) {
    return NextResponse.json({ error: 'Missing id' }, { status: 400 });
  }

  try {
    const provider = getProvider(providerName);
    const info = await provider.getPlayInfo(id, extra);
    return NextResponse.json(info);
  } catch {
    return NextResponse.json({ error: 'Failed to get url' }, { status: 500 });
  }
}
